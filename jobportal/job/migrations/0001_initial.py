# Generated by Django 3.0.4 on 2020-06-08 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=250)),
                ('no_of_vacancy', models.CharField(max_length=250)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('requirements', models.TextField()),
                ('salary', models.CharField(blank=True, max_length=250, null=True)),
                ('experience', models.CharField(blank=True, max_length=250, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_category', related_query_name='job_categories', to='job.JobCategory')),
                ('job_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', related_query_name='types', to='job.JobType')),
            ],
        ),
    ]
