from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import UserPassesTestMixin

class GroupRequiredMixin(UserPassesTestMixin):
  # login_url = 'account/login/'
  group_names = []

  def test_func(self):
    return self.request.user.groups.filter(name__in = self.group_names)

  def get_permission_denied_message(self):
    return "Must be {} to access this page".format(*self.group_names)


