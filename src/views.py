from django.shortcuts import render


def index(request):
    return (request, 'home.html', {})

