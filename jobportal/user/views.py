from django.contrib.auth import ( authenticate , get_user_model , login, logout )
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, Http404
import code
from custom_decorators.decorator import *

# Create your views here.
def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user=authenticate(username=username, password=password)
		login(request,user)

		if request.user.is_superuser==True:
			return HttpResponseRedirect(reverse('dashboard'))
		else:
			return HttpResponseRedirect(reverse('index'))


	context = {'form':form}
	return render(request,'user/login.html',context=context)

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('account:login'))

@group_required('Admin','login_url')
def register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		group=form.cleaned_data.get('user_group')
		user.set_password(password)
		user.save()
		if group:
			user.groups.add(group)

		return HttpResponseRedirect(reverse('account:list'))

	context={
		'form':form,
	}

	return render(request,'user/register.html',context=context)


@group_required('Admin','login_url')
def user_update_view(request,id):
	instance=get_object_or_404(User,id=id)
	form = EditUserForm(request.POST or None,instance=instance)
	if form.is_valid():
		user=form.save(commit=False)
		
		group=form.cleaned_data.get('user_group')
		user_type = Group.objects.get(name = group)
		user.save()
		instance.groups.clear()
		user.groups.add(user_type)
		return HttpResponseRedirect(reverse('account:list'))

	else:
		form=EditUserForm(request.POST or None,instance=instance)

	context={
		'form':form,
	}

	return render(request,'user/register.html',context=context)


# client side 
def signin_view(request):
	form = SignInForm(request.POST or None)
	print(form.errors)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)

		return HttpResponseRedirect(reverse('index'))

	context={
		'form':form,
	}

	return render(request,'client/signin.html',context=context)

#client side
def update_view(request,id):
	instance = get_object_or_404(User,id=id)
	if request.method =='POST':
		form = UpdateUserForm(request.POST, instance=instance)
		if form.is_valid():
			user=form.save(commit=False)
			user.save()

			return HttpResponseRedirect(reverse('account:profile', args = [instance.id]))
	else:
		form = UpdateUserForm(instance=instance)
	context={
		'form':form,
	}
	return render(request,'client/update_profile.html',context=context)


def user_detail_view(request,id=None):
	user = get_object_or_404(User,id=id)
	context={
		'user':user,
	}
	return render(request,'client/profile.html',context=context)


@group_required('Admin','login_url')
def user_list_view(request):
	users = User.objects.all()
	context={
		'users':users,
	}
	return render(request,'user/user_list.html',context=context)


@group_required('Admin','login_url')
def create_group(request):
	form=CreateGroupForm(request.POST or None)
	if form.is_valid():
		form.save()
	context={
		'form':form,
	}
	return render(request,'user/add_groups.html',context=context)


# @group_required('Admin','login_url')
# def update_group(request,id):
# 	instance=Group.objects.get(id=id)
# 	if request.method=="POST":
# 		form=CreateGroupForm(request.POST or None, instance=instance)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect(reverse('account:group-list'))
# 	else:
# 		form=CreateGroupForm(instance=instance)
# 	context={
# 		'form':form,
# 	}
# 	return render(request,'user/add_groups.html',context=context)


@group_required('Admin','login_url')
def group_list_view(request):
	groups = Group.objects.all()
	context={
		'groups':groups,
	}
	return render(request,'user/group_list.html',context=context)


# code.interact(local = dict(globals(), **locals())) 










