from django.urls import path
from accounts.views import UserRegisterView, UserEditView, PasswordsChangeView, password_success


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edite-profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='change-password'),
    path('password-success/', password_success, name='password-success')
]
