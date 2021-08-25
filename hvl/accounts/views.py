from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from accounts.forms import UserRegisterForm, UserEditProfileForm, UserEditPasswordForm
from django.urls import reverse_lazy

class IsSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class UserRegisterView(IsSuperuserMixin, CreateView):
    form_class = UserRegisterForm
    template_name= "registration/register.html"

class UserEditView(UpdateView):
    form_class = UserEditProfileForm
    template_name= "registration/edit-profile.html"

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = UserEditPasswordForm
    template_name = "registration/change-password.html"
    success_url = reverse_lazy('password-success')

def password_success(request):
    return render(request, 'registration/password-success.html')
