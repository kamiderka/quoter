from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.

class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
 
        