# Generated by Django 3.0.4 on 2020-07-03 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0007_resume_usereducationdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resume', related_query_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
    ]
