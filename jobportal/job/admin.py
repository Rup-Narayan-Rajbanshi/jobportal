from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(JobCategory)
admin.site.register(JobType)
admin.site.register(JobDetail)
admin.site.register(Applicant)
admin.site.register(Resume)