from django.shortcuts import render, redirect
from django.views import generic

from .forms import CreateUserForm

# Create your views here.

class RegisterView(generic.FormView):
    template_name = 'register.html'
    form_class = CreateUserForm
    success_url = '/'

    def form_valid(self, form):
        print('All Correct')
        form.save()
        return super().form_valid(form)
 
        