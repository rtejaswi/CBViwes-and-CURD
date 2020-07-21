from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from . import models
# Create your views here.

# class hello(View):
#     def get(self, request):
#         return HttpResponse('<h1>CLASS BASED VIEWS ARE COOL!</h1>')

class home(TemplateView):
    template_name = 'home.html'

# class index(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'Basic Injection! '
#         return context


class SchoolListView(ListView):
    context_object_name = 'schools' #otherwise school_list by default
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'myapp/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')
    template_name_suffix = '_update_form'

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('myapp:list')
