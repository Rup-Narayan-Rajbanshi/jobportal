from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			if field in ("username"):
				self.fields[field].widget.attrs.update({'placeholder':'Username'})
			if field in ("password"):
				self.fields[field].widget.attrs.update({'placeholder':'Password'})
			self.fields[field].label=''

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username,password=password)

		if not user:
			raise forms.ValidationError('The user doesnot exist')
		if not user.check_password(password):
			raise forms.ValidationError('The password is incorrect')
		if not user.is_active:
			raise forms.ValidationError('The user is not active')


class RegisterForm(forms.ModelForm):
	confirm_password=forms.CharField(label='Confirm Password')
	user_group=forms.ModelChoiceField(
        queryset = Group.objects.all(),
        required = False,
        label='Group',
    )
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			'confirm_password',
			'user_group',
			]

	def clean(self,*args,**kwargs):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError('Password must match')

class EditUserForm(forms.ModelForm):
	choices = [(group, group) for group in Group.objects.all()]
	user_group=forms.ChoiceField(
        choices = choices,
        required = False,
        label='Group',
    )
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'user_group',
			]


class SignInForm(forms.ModelForm):
	confirm_password=forms.CharField(label='Confirm Password')
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
			'confirm_password',
			]

	def clean(self,*args,**kwargs):
		password = self.cleaned_data.get('password')
		confirm_password = self.cleaned_data.get('confirm_password')
		if password != confirm_password:
			raise forms.ValidationError('Password must match')


class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			]

class CreateGroupForm(forms.ModelForm):
	class Meta:
		model=Group
		fields=('__all__')











