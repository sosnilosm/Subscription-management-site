from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView, LoginView
from users.utils import send_email_for_verify
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator as token_generator

User = get_user_model()


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    pass


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
    pass


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    pass


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
    pass


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    pass


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
    pass


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': CustomUserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('main')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user
