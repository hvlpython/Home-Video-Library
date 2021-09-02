from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegisterForm, UserEditProfileForm, UserEditPasswordForm
from django.urls import reverse_lazy
from django.core.mail import send_mail


class IsSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class IsUserNameMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.username


class UserRegisterView(IsSuperuserMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "registration/register.html"


class UserEditView(IsUserNameMixin, UpdateView):
    form_class = UserEditProfileForm
    template_name = "registration/edit-profile.html"

    def get_object(self):
        return self.request.user


class PasswordsChangeView(IsUserNameMixin, PasswordChangeView):
    form_class = UserEditPasswordForm
    template_name = "registration/change-password.html"
    success_url = reverse_lazy('password-success')


@login_required(login_url="/login/")
def password_success(request):
    return render(request, 'registration/password-success.html')


def user_register_request(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        send_mail(
            "Registration Message from " + username,
            "Please register my with the data: \n\n" "Username: " + username + "\n" + "First Name: " + first_name + "\n" +
            "Last Name: " + last_name + "\n" + "Email: " + email,
            email,
            ["hvlpython@gmail.com"]
        )

        return render(request, 'registration/user_register_request.html', {'username': username})

    else:
        return render(request, 'registration/user_register_request.html')
