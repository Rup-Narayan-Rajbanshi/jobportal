
from django.urls import path
from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView
from django_filters.views import FilterView
from . import views
# from apis.views import *

app_name = 'job'

urlpatterns = [
    path('category/add/', AddCategory.as_view(), name='add-category'),
    path('category/<int:pk>/update/', CategoryUpdate.as_view(), name='update-category'),
    path('category/list/', CategoryList.as_view(), name='category-list'),

    path('jobtype/add/', AddJobType.as_view(), name='add-jobtype'),
    path('jobtype/<int:pk>/update/', JobTypeUpdate.as_view(), name='update-jobtype'),
    path('jobtype/list/', JobTypeList.as_view(), name='jobtype-list'),

    path('add/', AddJobDetail.as_view(), name='add-job'),
    path('<int:pk>/update/', JobDetailUpdate.as_view(), name='update-job'),
    path('list/', JobDetailList.as_view(), name='job-list'),
    path('<int:pk>/detail', JobDetailView.as_view(), name='job-detail'),

    path('<int:pk>/apply/',JobApplication.as_view(),name='apply-job'),
    path('applications/',JobApplicationFilterView.as_view(),name='applications'),
    path('applications/<int:pk>/detail',JobApplicationDetailView.as_view(),name='application-details'),

    path('applicant_resume/<int:pk>/', ApplicantResumeDetailView.as_view(), name='applicant-resume'),

    path('set_interview/<int:id>/', set_interview, name='set-interview'),
    path('select/<int:id>/', select_candidate, name='select'),

#Client side

    path('<int:pk>/job_detail', HomeJobDetailView.as_view(), name='home-job-detail'),
    path('message', TemplateView.as_view(template_name='job_application/message.html'), name='message'),

    url(r'^job_list/$', FilterView.as_view(filterset_class=JobListFilterView,
        template_name='client/job_list.html'), name='home-job-list'),
    path('category/<int:pk>/', CategoryJobList.as_view(), name='category-jobs'),
    path('applied/', AppliedJobList.as_view(), name='applied-jobs'),
    path('create_resume/', ResumeCreateView.as_view(), name='create-resume'),
    path('resume/<int:pk>/update/', ResumeUpdate.as_view(), name='resume-update'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='resume'),


]
