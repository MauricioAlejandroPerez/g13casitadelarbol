from django.forms.forms import Form
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .forms import SignUpForm



# Create your views here.
class Login(auth_views.LoginView):
    '''Vista de login de usuario'''
    template_name = 'login.html'
    success_url = reverse_lazy('apps.noticias_app:index')

class Logout(LoginRequiredMixin, auth_views.LogoutView):
    '''Vista de logout/Cierre de sesion de usuario'''
    template_name = 'registration/logout.html'

class SignUpView(FormView):
    '''Vista de registro de usuario'''
    template_name = 'registration/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('apps.blog_auth:registercomplete')

    def form_valid(self, form):
        '''Verificamos que los datos sean validos, luego los enviamos'''
        form.save()
        return super().form_valid(form)

class WelcomneView(CreateView):
    template_name = 'welcome.html'