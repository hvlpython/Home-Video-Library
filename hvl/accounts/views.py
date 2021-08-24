from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from accounts.forms import UserRegisterForm

class IsSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class UserRegisterView(IsSuperuserMixin, CreateView):
    form_class = UserRegisterForm
    template_name= "registration/register.html"
