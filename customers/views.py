import json

from django.contrib.admin.templatetags.admin_list import results
from pyexpat import model

from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Person

def index(request):
    persons = Person.objects.all()
    return render(request, 'customers.html', {'persons': persons})


def detail(request, question_id):
    question = question_id
    if question < 1:
        question = 1
    return render(request, 'customers_detail.html', {'question': question})

