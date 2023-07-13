from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path


app_name = 'user'

urlpatterns = [
    path('logout/',
         LogoutView.as_view(template_name='user/logged_out.html'),
         name='logout'
         ),
    path(
        'login/',
        LoginView.as_view(template_name='user/login.html'),
        name='login'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='user/password_change_form.html'
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='user/password_change_done.html'
        ),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='user/password_reset_form.html'
        ),
        name='password_reset_form'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='user/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='user/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'auth/reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='user/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
