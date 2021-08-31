from django.urls import path
from accounts.views import UserRegisterView, UserEditView, PasswordsChangeView, password_success, user_register_request
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edite-profile/', UserEditView.as_view(), name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(), name='change-password'),
    path('password-success/', password_success, name='password-success'),
    
    path('reset_password/', 
        PasswordResetView.as_view(template_name='registration/password_reset.html'), 
        name='reset_password'),
    
    path('password_reset/done/', 
        PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), 
        name='reset_password_sent'),

    path('reset/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(), 
        name='password_reset_confirm'),

    path('reset/done/', 
        PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
        name='password_reset_complete'),

    path('user_register_request/', user_register_request, name='user_register_request'),


]
