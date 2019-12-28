import json

from django.contrib.admin.templatetags.admin_list import results
from django.db.models import Q
from django.forms import forms
from django.views.generic import ListView
from pyexpat import model

from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Person
from .forms import PersonForm


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


def person_detail(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    form = PersonForm()
    return render(request, 'form.html', {'form': form})


def edit(request, id=None, template_name='form.html'):
    id = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, instance=id)
    if form.is_valid():
        form.save(commit=False)

    return render(request, 'form.html', {'form': form})
