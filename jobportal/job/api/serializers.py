from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)
from job.models import JobDetail, Applicant, Resume

class JobCreateSerializer(ModelSerializer):
	
	class Meta:
		model=JobDetail
		fields=[
			'category',
			'job_type',
			'company',
			'location',
			'position',
			'no_of_vacancy',
			'salary',
			'experience',
			]


class JobListSerializer(ModelSerializer):
	url=HyperlinkedIdentityField(
		view_name='job-api:detail',
		lookup_field='pk'
		)

	user=SerializerMethodField()
	category=SerializerMethodField()
	job_type=SerializerMethodField()
	logo=SerializerMethodField()
	class Meta:
		model=JobDetail
		fields=[
			'url',
			'user',
			'category',
			'job_type',
			'company',
			'logo',
			'location',
			'position',
			'no_of_vacancy',
			'salary',
			'experience',
			]

	def get_user(self,obj):
		return str(obj.user.username)

	def get_category(self,obj):
		return str(obj.category.category)

	def get_job_type(self,obj):
		return str(obj.job_type.job_type)

	def get_logo(self,obj):
		try:
			logo=obj.logo.url
		except:
			logo=None

		return logo



class ApplicationListSerializer(ModelSerializer):
	resume=HyperlinkedIdentityField(
		view_name='job-api:resume',
		lookup_field='pk'
		)

	company=SerializerMethodField()
	job=SerializerMethodField()
	class Meta:
		model=Applicant
		fields=[
			'job',
			'company',
			'name',
			'resume',
			'education',
			'experience',
			'skills',
			'set_interview',
			'select'
			]

	def get_job(self,obj):
		return str(obj.job.position)

	def get_company(self,obj):
		return str(obj.job.company)


class ResumeListSerializer(ModelSerializer):
	
	class Meta:
		model=Resume
		exclude=('id','user',)