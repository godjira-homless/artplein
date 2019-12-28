import json

from django.contrib.admin.templatetags.admin_list import results
from django.db.models import Q
from django.forms import forms
from django.views.generic import ListView
from pyexpat import model

from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Person
from django.core import validators


def index(request):
    persons = Person.objects.all()
    return render(request, 'customers.html', {'persons': persons})


def detail(request, question_id):
    question = question_id
    entry = Person.objects.get(pk=question)
    if question < 1:
        question = 1

    rt = {'id': question, 'fn': entry.first_name, 'ln': entry.last_name}

    return render(request, 'customers_detail.html', {'rt': rt})


class SearchResultsView(ListView):
    model = Person
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Person.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        return object_list

