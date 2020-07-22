# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import (
    FormView, 
    FormMixin,
    CreateView,
    UpdateView,
)
from django.views.generic import DetailView, ListView
from .models import *
from .forms import *
from custom_decorators.decorator import *
from django.db.models import Q
import code
from django.contrib import messages
import django_filters
from .utils import *
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required,user_passes_test
from core.views import *


# Create your views here. 
#************************ Category ************************#
@method_decorator(login_required(), name = "dispatch")
class AddCategory(GroupRequiredMixin,CreateView):
    group_names=['Admin']
    model = JobCategory
    fields = ('__all__')
    template_name = 'jobcategory/add.html'

    def get_success_url(self):
        return reverse('job:category-list')


@method_decorator(login_required(), name = "dispatch")
class CategoryUpdate(GroupRequiredMixin,UpdateView):
    group_names=['Admin']
    model = JobCategory
    fields = ('__all__')
    template_name = 'jobcategory/add.html'

    def get_success_url(self):
        return reverse('job:category-list')


@method_decorator(login_required(), name = "dispatch")
class CategoryList(GroupRequiredMixin,ListView):
    group_names=['Admin']
    model = JobCategory
    template_name = 'jobcategory/list.html'
    context_object_name = 'jobcategories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#*************************Category End ***************************#


#************************ JobType ************************#
@method_decorator(login_required(), name = "dispatch")
class AddJobType(GroupRequiredMixin,CreateView):
    group_names=['Admin']
    model = JobType
    fields = ('__all__')
    template_name = 'jobtypes/add.html'

    def get_success_url(self):
        return reverse('job:jobtype-list')

@method_decorator(login_required(), name = "dispatch")
class JobTypeUpdate(GroupRequiredMixin,UpdateView):
    group_names=['Admin']
    model = JobType
    fields = ('__all__')
    template_name = 'jobtypes/add.html'

    def get_success_url(self):
        return reverse('job:jobtype-list')


@method_decorator(login_required(), name = "dispatch")
class JobTypeList(GroupRequiredMixin,ListView):
    group_names=['Admin']
    model = JobType
    template_name = 'jobtypes/list.html'
    context_object_name = 'jobtypes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#*************************Type End ***************************#


#*************************Job Detail  ***************************#
@method_decorator(login_required(), name = "dispatch")
class AddJobDetail(GroupRequiredMixin,CreateView):
    group_names=['Company','Admin']
    model = JobDetail
    form_class = JobDetailForm
    template_name = 'job/add.html'

    def get_success_url(self):
        return reverse('job:job-list')

    def form_valid(self,forms):
        job=forms.save(commit=False)
        logo=forms.cleaned_data['logo']
        job.logo=logo
        job.user=self.request.user
        # code.interact(local = dict(globals(), **locals())) 
        job.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required(), name = "dispatch")
class JobDetailUpdate(GroupRequiredMixin,UpdateView):
    group_names=['Company','Admin']
    model = JobDetail
    form_class = JobDetailForm
    template_name = 'job/add.html'

    def get_success_url(self):
        return reverse('job:job-list')


@method_decorator(login_required(), name = "dispatch")
class JobDetailList(GroupRequiredMixin,ListView):
    group_names=['Company','Admin']
    model = JobDetail
    template_name = 'job/list.html'
    context_object_name = 'jobs'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name ='Admin'):
            context['jobs']=JobDetail.objects.all()
        else:
            context['jobs']=JobDetail.objects.filter(user=self.request.user)
        return context

@method_decorator(login_required(), name = "dispatch")
class JobDetailView(GroupRequiredMixin,DetailView):
    group_names=['Company','Admin']
    model = JobDetail
    context_object_name = "job"
    template_name = "job/detail.html"


#************************* Job Detail End  ***************************#


#************************* Job Application  ***************************#

class JobApplication(CreateView):
    model = Applicant
    template_name = "job_application/application_form.html"
    form_class = JobApplicationForm

    def get_success_url(self):
        return reverse('job:applied-jobs')

    def get_form_kwargs(self):
        if not self.request.user.is_anonymous:
           self.initial = {'name':self.request.user.first_name +" "+ self.request.user.last_name,}
        return super().get_form_kwargs()

    def dispatch(self, request, *args, **kwargs):
        try: 
            self.job = JobDetail.objects.get(id = self.kwargs['pk'])
        except:
            self.job = None
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self,forms):
        job_application=forms.save(commit=False)
        job_application.job=self.job
        job_application.user=self.request.user
        job_application.save()
        messages.success(self.request, "Application sent successfully.")
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required(), name = "dispatch")
class ApplicationList(GroupRequiredMixin,ListView):
    group_names=['Company','Admin']
    model=Applicant
    template_name = 'job_application/list.html'
    context_object_name ='applications'
    paginate_by = 50


@method_decorator(login_required(), name = "dispatch")
class JobApplicationDetailView(GroupRequiredMixin,DetailView):
    group_names=['Company','Admin']
    model = Applicant
    context_object_name = "job_application"
    template_name = "job_application/detail.html"


@method_decorator(login_required(), name = "dispatch")
class JobApplicationFilterView(GroupRequiredMixin,FormMixin, ListView):
    group_names=['Company','Admin']
    query = None
    model = Applicant
    form_class = ApplicationSearchForm
    template_name = "job_application/list.html"
    context_object_name = "applications"
    paginate_by = 50


    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # code.interact(local = dict(globals(), **locals()))
        if 'download' in request.GET:
          return self.download(self.get_queryset())

        return response
  

    def get_queryset(self):
        self.query = self.request.GET
        if len(self.query) > 0:
          return self.filter()
        else:
            # code.interact(local = dict(globals(), **locals()))
            if self.request.user.groups.filter(name ='Admin'):
                return self.model.objects.all()
            else:
                return self.model.objects.filter(job__user=self.request.user)

    def download(self, qs):
        # code.interact(local = dict(globals(), **locals()))
        return download_reports(self.request, qs, name='job_applications')

    def filter(self):
        self.initial = self.query.copy()
        query = self.query

        name = query.get("name")
        education = query.get("education")
        company = query.get("company")
        set_interview=query.get("set_interview")
        select=query.get("select")

        if set_interview=='Yes':
            set_interview=True
        else:
            set_interview=False

        if select=='Yes':
            select=True
            set_interview=True
        else:
            select=False
        # code.interact(local = dict(globals(), **locals()))
        if self.request.user.groups.filter(name ='Admin'):
            return self.model.objects.filter(job__company__icontains=company or "",
                                         name__icontains=name or "",
                                         education__contains=education or "",
                                         set_interview__icontains=set_interview,
                                         select__icontains=select
                                         )
        else:
            return self.model.objects.filter(job__company__icontains=company or "",
                                         name__icontains=name or "",
                                         education__contains=education or "",
                                         set_interview__icontains=set_interview,
                                         select__icontains=select,
                                         job__user=self.request.user
                                         )


#*************************Job Applicaton End  ***************************#

#Dashboard
@method_decorator(login_required(), name = "dispatch")
class Dashboard(ListView):
    group_names=['Company','Admin']
    model = JobDetail
    template_name = 'admin_panel.html'
    # context_object_name = 'jobs'

    def get_context_data(self,*args, **kwargs):
        context = super(Dashboard, self).get_context_data(*args, **kwargs)
        if self.request.user.groups.filter(name='Admin'):
            context['jobs'] = JobDetail.objects.filter(expired=False)[:10]
            context['applications'] = Applicant.objects.all().filter(job__expired=False)[:10]
        else:
            context['jobs'] = JobDetail.objects.filter(user=self.request.user,expired=False)[:10]
            context['applications'] = Applicant.objects.filter(job__user=self.request.user,job__expired=False)[:10]
        return context

       


#************************** Client Side **********************************#


class Home(FormMixin,ListView):
    query=None
    model = JobDetail
    form_class=JobSearchFormIndex
    template_name = 'index.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        self.query = self.request.GET
        query=self.query.get('search_field')
        if len(self.query) > 0:
            self.initial = self.query.copy()
            return self.model.objects.filter(
                Q(company=query)|
                Q(category__category__icontains=query)|
                Q(job_type__job_type__icontains=query)|
                Q(position__icontains=query)
                )
        else:
          return self.model.objects.all().filter(expired=False)[:15]


    def get_context_data(self,*args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['categories'] = JobCategory.objects.all()
        context['feature_jobs'] = JobDetail.objects.all().filter(expired=False)[:5]

        return context

class HomeJobDetailView(DetailView):
    model = JobDetail
    context_object_name = "job"
    template_name = "client/job_detail.html"


class JobListFilterView(django_filters.FilterSet):
    company = django_filters.CharFilter(
                                        lookup_expr='icontains',
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Company',
                                            'class':'mr-3 form-control px-4'})
                                            )
    category = django_filters.ModelChoiceFilter(
                                        queryset=JobCategory.objects.all(),
                                        widget=forms.Select(attrs={
                                            'class':'mr-3 form-control px-4'})
                                        )
    job_type = django_filters.ModelChoiceFilter(
                                        queryset=JobType.objects.all(),
                                        widget=forms.Select(attrs={
                                            'class':'mr-3 form-control px-4'})
                                        )
    class Meta:
        model = JobDetail
        fields = ['category', 'job_type', 'company' ]
        


# filter according to category

class CategoryJobList(ListView):
    category=None
    model=JobDetail
    template_name="client/category_jobs.html"
    context="jobs"

    def dispatch(self, request, *args, **kwargs):
        try: 
            self.category = self.kwargs['pk']
            # code.interact(local = dict(globals(), **locals()))
        except:
            self.category = None
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self,*args, **kwargs):
        context = super(CategoryJobList, self).get_context_data(*args, **kwargs)
        context['category_jobs'] = JobDetail.objects.filter(category=self.category)

        return context



class AppliedJobList(ListView):
    category=None
    model=Applicant
    template_name="client/applied_jobs.html"
    paginate_by = 10

    def get_context_data(self,*args, **kwargs):
        context = super(AppliedJobList, self).get_context_data(*args, **kwargs)
        context['applications'] = Applicant.objects.filter(user=self.request.user)

        return context


class ResumeCreateView(CreateView):
    resume=None
    model = Resume
    template_name = "client/resume.html"
    form_class = ResumeForm

    def get_success_url(self):
        return reverse('job:resume', args = [self.resume])

    def form_valid(self,forms):
        resume=forms.save(commit=False)
        resume.user=self.request.user
        resume.save()
        self.resume=resume.id
        return HttpResponseRedirect(self.get_success_url())


class ResumeUpdate(UpdateView):
    resume=None
    model = Resume
    fields = ('__all__')
    template_name = 'client/resume.html'

    def dispatch(self, request, *args, **kwargs):
        try: 
            self.resume = self.kwargs['pk']
        except:
            self.resume = None
        return super().dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return reverse('job:resume', args = [self.resume])

    def form_valid(self,forms):
        resume=forms.save(commit=False)
        resume.user=self.request.user
        resume.save()
        return HttpResponseRedirect(self.get_success_url())



class ResumeDetailView(DetailView):
    model = Resume
    context_object_name = "resume"
    template_name = "client/resume_detail.html"


@method_decorator(login_required(), name = "dispatch")
class ApplicantResumeDetailView(GroupRequiredMixin,DetailView):
    group_names=['Company','Admin']
    model = Resume
    context_object_name = "resume"
    template_name = "job_application/applicant_resume.html"



@group_required('Admin','Company','login_url')
def set_interview(request,id):
    applicant=Applicant.objects.get(id=id)
    applicant.set_interview=True
    applicant.save()
    # code.interact(local = dict(globals(), **locals()))
    # messages.success(request, "Applicant selected for interview.")
    return HttpResponseRedirect(reverse('job:applications'))

@group_required('Admin','Company','login_url')
def select_candidate(request,id):
    applicant=Applicant.objects.get(id=id)
    applicant.select=True
    applicant.save()
    # messages.success(request, "Applicant selected for Job.")
    return HttpResponseRedirect(reverse('job:applications'))

