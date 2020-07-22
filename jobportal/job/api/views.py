from django.db.models import Q
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
	)
from rest_framework.generics import (
	ListAPIView,
	CreateAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView
	)
from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination
	)

from.pagination import JobLimitOffsetPagination, JobPageNumberPagination
from rest_framework.permissions import IsAdminUser

from .permissions import IsOwnerOrReadOnly
from job.models import JobDetail, Applicant, Resume
from .serializers import (
	JobListSerializer,
	JobCreateSerializer,
	ApplicationListSerializer,
	ResumeListSerializer
	)

class JobListAPIView(ListAPIView):
	# queryset=JobDetail.objects.all()
	serializer_class=JobListSerializer
	filter_backends=[SearchFilter,OrderingFilter]
	search_fields=['company','location','position','category__category','user__username']
	pagination_class=JobPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		queryset_list=JobDetail.objects.all()
		query=self.request.GET.get('q')
		if query:
			queryset_list=JobDetail.objects.filter(
				Q(company__icontains=query)|
				Q(location__icontains=query)|
				Q(position__icontains=query)
				)
		return queryset_list



class JobCreateAPIView(CreateAPIView):
	queryset=JobDetail.objects.all()
	serializer_class=JobCreateSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class JobDetailAPIView(RetrieveAPIView):
	queryset=JobDetail.objects.all()
	serializer_class=JobListSerializer

class JobUpdateAPIView(RetrieveUpdateAPIView):
	queryset=JobDetail.objects.all()
	serializer_class=JobCreateSerializer
	permission_classes=[IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


class JobDeleteAPIView(DestroyAPIView):
	queryset=JobDetail.objects.all()
	serializer_class=JobListSerializer



class ApplicationListAPIView(ListAPIView):
	serializer_class=ApplicationListSerializer
	filter_backends=[SearchFilter,OrderingFilter]
	search_fields=['job__position','job__company']
	pagination_class=JobPageNumberPagination

	def get_queryset(self, *args, **kwargs):
		queryset_list=Applicant.objects.all()
		query=self.request.GET.get('q')
		if query:
			queryset_list=Applicant.objects.filter(
				Q(job__position__icontains=query)|
				Q(job__company__icontains=query)
				)
		return queryset_list


class ResumeAPIView(RetrieveAPIView):
	queryset=Resume.objects.all()
	serializer_class=ResumeListSerializer