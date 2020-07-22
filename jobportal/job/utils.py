from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import csv
import code


def download_reports(request, queryset, name):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(name)  
    field_names = ['job','name','education','set_interview','select']
    
    writer = csv.writer(response)
    writer.writerow(map(lambda field: field.replace("_", " ").upper(), field_names))
    
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response

