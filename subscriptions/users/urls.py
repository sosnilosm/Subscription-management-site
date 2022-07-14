from django.urls import path, include
from django.views.generic import TemplateView

from .views import CustomLoginView, Register, CustomPasswordResetView, CustomPasswordResetDoneView, \
    CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomPasswordChangeView, \
    CustomPasswordChangeDoneView, EmailVerify


urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),

    path('', include('django.contrib.auth.urls')),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('register/', Register.as_view(), name='register'),
    path(
        'confirm_email/',
        TemplateView.as_view(template_name='registration/confirm_email.html'),
        name='confirm_email'
    ),
    path(
        'verify_email/<uidb64>/<token>/',
        EmailVerify.as_view(),
        name='verify_email'
    ),
    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='registration/invalid_verify.html'),
        name='invalid_verify'
    ),
]
