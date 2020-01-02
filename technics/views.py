from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse

from .forms import TechnicMofelForm
from .models import Technic
from .filters import TechnicFilter

class TechnicCreateView(CreateView):
    template_name = 'technic_create.html'
    form_class = TechnicMofelForm
    queryset = Technic.objects.all()
    #success_url '/' # another ovverride the url

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self): #override the url
    #    return '/'

class TechnicUpdateView(UpdateView):
    template_name = 'technic_create.html'
    form_class = TechnicMofelForm
    #success_url '/' # another ovverride the url

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Technic, slug=slug_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self): #override the url
    #    return '/'

class TechnicListView(ListView):
    model = Technic
    template_name = 'technic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TechnicFilter(self.request.GET, queryset=self.get_queryset())
        return context

    queryset = Technic.objects.all()


class TechnicDetailView(DetailView):
    model = Technic
    template_name = 'technic_detail.html'
    queryset = Technic.objects.all()




class TechnicDeleteView(DeleteView):
    template_name = 'technic_delete.html'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Technic, slug=slug_)

    def get_success_url(self):
        return reverse('technic_list')
