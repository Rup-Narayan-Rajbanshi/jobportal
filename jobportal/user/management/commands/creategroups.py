# Create permission groups
# Create permissions (read only) to models for a set of groups
import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist

GROUPS = ['Company', 'Admin','Job Seeker']

# MODELS = ['profile', 'user', 'Company', 'location', 'location type']

# PERMISSIONS = ['view', 'add', 'change', 'delete']


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        for group in GROUPS:
            try:
                new_group = Group.objects.get(name = group)
            except ObjectDoesNotExist:
                new_group = Group.objects.create(name = group)                
            group_name = new_group.name
            # new_group, created = Group.objects.get_or_create(name=group)
            # for model in MODELS:
            #     for permission in PERMISSIONS:
                    
            #         name = 'Can {} {}'.format(permission, model)
            #         print("Creating {}".format(name))

            #         try:
            #             model_add_perm = Permission.objects.get(name=name)
            #         except Permission.DoesNotExist:
            #             logging.warning("Permission not found with name '{}'.".format(name))
            #             continue

            #         new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")