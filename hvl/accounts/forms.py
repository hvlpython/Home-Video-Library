from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField

class UserRegisterForm(UserCreationForm):
    email = EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = CharField(max_length=128, widget=forms.TimeInput(attrs={"class": "form-control"}))
    last_name = CharField(max_length=128, widget=forms.TimeInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"