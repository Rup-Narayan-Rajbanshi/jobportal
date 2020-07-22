from django import forms
from .models import *

class JobDetailForm(forms.ModelForm):
    class Meta:
        model = JobDetail
        exclude=('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'deadline':
                self.fields['deadline'].widget.attrs.update({"class":"form-control-sm datepicker"})

class JobApplicationForm(forms.ModelForm):
	class Meta:
		model = Applicant
		# fields=('applicant__user,applicant__education','applicant__experience',)
		# fields=('__all__')
		exclude=('user','job','set_interview','select',)


class ApplicationSearchForm(forms.Form):
    SET_INTERVIEW = [("No","No"),("Yes","Yes")]

    SELECT = [("No","No"),("Yes","Yes")]

    set_interview=forms.ChoiceField(
        choices = SET_INTERVIEW,
        required = False,
        label='Interview Set',

    )
    select=forms.ChoiceField(
        choices = SELECT,
        required = False,
        label='Selected',
    )
    company = forms.CharField(
        required = False,
        label='Company',
    )
    name = forms.CharField(
        required = False,
        label='Name',
    )
    education = forms.CharField(
        required = False,
        label='Education',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control border-1'})


class JobSearchForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset = JobCategory.objects.all(),
        required = False,
        label='Job Category',
    )
    job_type = forms.ModelChoiceField(
        queryset = JobType.objects.all(),
        required = False,
        label='Job Type',
    )
    company = forms.CharField(
        required = False,
        label='Company',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'mr-3 form-control border-0 px-4'})


class JobSearchFormIndex(forms.Form):
    search_field = forms.CharField(
        required = False,
        label='',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'mr-3 form-control border-0 px-4',
                                                    'placeholder':'Job title, Company, Category'}
                                                    )

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields=('__all__')

    # date = forms.DateField(
    #   label='',
    #   required=False,
    #   )

    # date_to = forms.DateField(
    #   label='',
    #   required=False,
    #   )
    # branch = forms.ModelChoiceField(
    #     queryset = CompanyBranch.objects.all(),
    #     required = False,
    #     label='',
    # )
    # company = forms.ModelChoiceField(
    #     queryset = Company.objects.all(),
    #     required = False,
    #     label='',
    # )

    # department = forms.ModelChoiceField(
    #     label = '',
    #     queryset = Department.objects.all(),
    #     required = False,
    # )



# class JobTypeForm(forms.ModelForm):
# 	class Meta:
# 		model = JobType
# 		fields=('__all__')


# class JobDetailForm(forms.ModelForm):
# 	class Meta:
# 		model = JobDetail
# 		fields=('__all__')


