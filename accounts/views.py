from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.generic import CreateView, UpdateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.views import (
    LoginView, LogoutView,
    )
from .models import User
from .forms import UserAdminCreationForm


class IndexView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/index.html'
    login_url = reverse_lazy('accounts:login')
    
    def get_object(self):
        return self.request.user


class Login(LoginView):

    model = User
    template_name = 'accounts/login.html'


class Logout(LogoutView):

    template_name = 'accounts/logged_out.html'


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        messages.info(
            self.request, "Cadastro realizado com sucesso! Faça seu login."
        )
        return super().form_valid(form)

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Django E-commerce',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@exemple.com",
                            [user.email],
                            fail_silently=False
                        )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    
                    return redirect('accounts:password_reset_done')
    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="accounts/password/password_reset.html",
        context={
            "form":form,
        })

class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)




login = Login.as_view()
logout = Logout.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
index = IndexView.as_view()
