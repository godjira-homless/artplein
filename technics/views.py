from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse

from .models import Technic

class TechnicListView(ListView):
    model = Technic
    template_name = 'technic_list.html'


class TechnicDetailView(DetailView):
    model = Technic
    template_name = 'technic_detail.html'

class TechnicDeleteView(DeleteView):
    template_name = 'technic_delete.html'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Technic, slug=slug_)

    def get_success_url(self):
        return reverse('technic_list')