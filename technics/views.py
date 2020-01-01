from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Technic

class TechnicListView(ListView):
    model = Technic
    template_name = 'technic_list.html'


class TechnicDetailView(DetailView):
    model = Technic
    template_name = 'technic_detail.html'

