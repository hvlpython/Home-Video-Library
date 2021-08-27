from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, TextInput, EmailInput, PasswordInput

class UserRegisterForm(UserCreationForm):
    email = EmailField(widget=EmailInput(attrs={"class": "form-control"}))
    first_name = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    last_name = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["type"] = "password"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["type"] = "password"

class UserEditProfileForm(UserChangeForm):
    email = EmailField(widget=EmailInput(attrs={"class": "form-control"}))
    first_name = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    last_name = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))
    username = CharField(max_length=128, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

class UserEditPasswordForm(PasswordChangeForm):
    old_password = CharField(max_length=128, widget=PasswordInput(attrs={"class": "form-control", "type":"password"}))
    new_password1 = CharField(max_length=128, widget=PasswordInput(attrs={"class": "form-control","type":"password"}))
    new_password2 = CharField(max_length=128, widget=PasswordInput(attrs={"class": "form-control","type":"password"}))

    class Meta:
        model = User
        fields = ("old_password", 'new_password1', 'new_password2')
