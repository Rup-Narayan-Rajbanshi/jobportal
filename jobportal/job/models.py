from django.db import models
from django.conf import settings

# Create your models here.
class JobCategory(models.Model):
	category=models.CharField(max_length=250)

	def __str__(self):
		return self.category


class JobType(models.Model):
	job_type=models.CharField(max_length=250)

	def __str__(self):
		return self.job_type	


class JobDetail(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.CASCADE,
							related_name='job',
							related_query_name='jobs',
							null=True,
							blank=True
							)
	category=models.ForeignKey(JobCategory,
							on_delete=models.CASCADE,
							related_name='job_category',
							related_query_name='job_categories',
							null=True,
							)
	job_type=models.ForeignKey(JobType,
							on_delete=models.CASCADE,
							related_name='type',
							related_query_name='types',
							null=True,
							)
	company=models.CharField(max_length=250)
	location=models.CharField(max_length=250)
	logo=models.FileField(null=True, blank=True)
	position=models.CharField(max_length=250)
	no_of_vacancy=models.CharField(max_length=250)
	description=models.TextField()
	requirements=models.TextField()
	salary=models.CharField(max_length=250,null=True,blank=True)
	experience=models.CharField(max_length=250,null=True,blank=True)
	deadline=models.DateField(null=True,blank=True)
	expired=models.BooleanField(default=False)
	created_date= models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.company+", "+self.position

	class Meta:
		ordering = ['-id',]



class Applicant(models.Model):
	job=models.ForeignKey(JobDetail,
						on_delete=models.CASCADE,
						related_name="applicant",
						related_query_name="applicants"
						)
	user=models.ForeignKey(settings.AUTH_USER_MODEL,
							on_delete=models.CASCADE,
							related_name="applicant",
							related_query_name="applicants",
							null=True,
							blank=True
							)
	name=models.CharField(max_length=500)
	education=models.CharField(max_length=500)
	experience=models.CharField(max_length=500)
	skills=models.TextField(null=True,blank=True)
	cv=models.FileField(null=True,blank=True)
	letter=models.TextField(null=True,blank=True)
	set_interview=models.BooleanField(default=False)
	select=models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-id',]



class Resume(models.Model):
	MALE = "M"
	FEMALE = "F"
	OTHER = "O"
	GENFER_CHOICES = (
		(MALE, "MALE"),
		(FEMALE, "FEMALE"),
		(OTHER, "OTHER"),
		)

	user=models.OneToOneField(settings.AUTH_USER_MODEL,
							on_delete=models.CASCADE,
							related_name='resume',
							related_query_name='resumes',
							null=True,
							blank=True
							)
	name=models.CharField(max_length=500)
	gender = models.CharField(max_length = 10,choices = GENFER_CHOICES)
	current_address=models.CharField(max_length=500,null=True,blank=True)
	permanent_address=models.CharField(max_length=500,null=True,blank=True)
	dob=models.DateField(null=True,blank=True)
	languages=models.CharField(max_length=500,null=True,blank=True)
	Hobbies=models.CharField(max_length=500,null=True,blank=True)
	martial_status=models.CharField(max_length=250,null=True,blank=True)
	phone_no=models.BigIntegerField(null=True,blank=True)
	website=models.CharField(max_length=500,null=True,blank=True)
	# education=models.CharField(max_length=500,null=True,blank=True)
	# percentage=models.CharField(max_length=10,null=True,blank=True)
	skills=models.TextField(null=True,blank=True)
	training_and_certification=models.CharField(max_length=500,null=True,blank=True)
	experience=models.CharField(max_length=500,null=True,blank=True)
	# company=models.CharField(max_length=500,null=True,blank=True)
	# experience=models.CharField(max_length=500,null=True,blank=True)
	project_description=models.TextField(null=True,blank=True)
	project_link=models.TextField(null=True,blank=True)

	def __str__(self):
		return self.name


class UserEducationDetail(models.Model):
	resume=models.ForeignKey(Resume,models.CASCADE)
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	qualification=models.CharField(max_length=250,null=True,blank=True)
	percentage_or_gpa=models.CharField(max_length=10,null=True,blank=True)


class JobApplication(models.Model):
	job=models.ForeignKey(JobDetail,on_delete=models.CASCADE)
	# user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	applicant=models.ForeignKey(Applicant,on_delete=models.CASCADE,null=True,blank=True)
	# cv=models.FileField(null=True,blank=True)
    
