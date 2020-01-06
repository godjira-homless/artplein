from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import AjaxForm
from .models import Ajax
from artists.models import Artist
from technics.models import Technic
import json


def ajax_list(request):
    items = Ajax.objects.all()
    context = {'items': items}
    return render(request, 'ajax_list.html', context)


def create_ajax(request):
    if request.method == 'POST':
        form = AjaxForm(request.POST)
        if form.is_valid():
            code = request.POST.get("code")
            title = request.POST.get("title")
            artist_name = request.POST.get("artist")
            #artist_name = "Nagy Sándor"
            artist, created = Artist.objects.get_or_create(name=artist_name)
            print(artist_name)
            print(artist)
            tech = request.POST.get("tech")
            tech = Technic.objects.get(id=tech)
            description = request.POST.get("description")

            menu = Ajax.objects.create(
                code=code,
                title=title,
                artist=artist,
                tech=tech,
                description=description
            )

            menu.save()

    form = AjaxForm()
    return render(request, 'ajax_create.html', {'form': form})
