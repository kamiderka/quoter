from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from .forms import RegisterUserForm

# Create your views here.

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = '/login'

    def form_valid(self, form):
        print('All Correct')
        form.save()
        return super().form_valid(form)
 
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('homepage')
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)
   