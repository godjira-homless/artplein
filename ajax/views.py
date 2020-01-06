from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import AjaxForm
from .models import Ajax
from artists.models import Artist
from technics.models import Technic
import json

def contact_name_search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        names = Artist.objects.filter(Q(name__icontains=q))
        result = []
        for n in names:
            name_json = n.name
            result.append(name_json)
        data = json.dumps(result)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

    context = {}
    return render(request, 'ajax_create.html', context)

def ajax_list(request):
    items = Ajax.objects.all()
    context = {'items': items}
    return render(request, 'ajax_list.html', context)


def create_ajax_old(request):
    if request.method == 'POST':
        form = AjaxForm(request.POST)
        if form.is_valid():
            code = request.POST.get("code")
            title = request.POST.get("title")
            artist_name = request.POST.get("artist")
            artist, created = Artist.objects.get_or_create(name=artist_name)
            # person, created = Person.objects.update_or_create(
            #    identifier=identifier, defaults={"name": name}
            # )
            tech = request.POST.get("tech")
            tech = Technic.objects.get(id=tech)
            description = request.POST.get("description")

            form = Ajax.objects.create(
                code=code,
                title=title,
                artist=artist,
                tech=tech,
                description=description
            )

            form.save()

    form = AjaxForm()
    return render(request, 'ajax_create.html', {'form': form})


def create_ajax(request):
    if request.method == 'POST':
        form = AjaxForm(request.POST)
        if form.is_valid():
            item = form.save()
            artist_name = request.POST.get("artist")
            item.artist, created = Artist.objects.get_or_create(name=artist_name)

            item.save()

    form = AjaxForm()
    return render(request, 'ajax_create.html', {'form': form})
