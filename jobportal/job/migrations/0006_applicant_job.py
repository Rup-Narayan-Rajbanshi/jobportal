# Generated by Django 3.0.4 on 2020-06-22 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200622_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.JobDetail'),
            preserve_default=False,
        ),
    ]