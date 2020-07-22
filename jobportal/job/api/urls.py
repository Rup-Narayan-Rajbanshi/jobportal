from django.urls import path
from .views import *
# from apis.views import *

app_name = 'job-api'

urlpatterns = [
    path('create/',JobCreateAPIView.as_view(),name='create'),
    path('list/',JobListAPIView.as_view(),name='list'),
    path('application/list/',ApplicationListAPIView.as_view(),name='applications'),
    path('resume/<int:pk>/',ResumeAPIView.as_view(),name='resume'),
    path('<int:pk>/',JobDetailAPIView.as_view(),name='detail'),
    path('<int:pk>/update/',JobUpdateAPIView.as_view(),name='update'),
    path('<int:pk>/delete/',JobDeleteAPIView.as_view(),name='delete'),

]