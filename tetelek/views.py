import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Tetelek, Artist
from .forms import TetelekForm

@login_required
def tetelek_list(request):
    tetelek = Tetelek.objects.all()
    context = {'items': tetelek}
    return render(request, 'tetelek_list.html', context)

@login_required
def create_tetelek(request):
    form = TetelekForm(request.POST or None, request.FILES)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.created_by = us
        form.save()
        return HttpResponseRedirect(reverse('tetelek_list'))
    form = TetelekForm()
    return render(request, 'create_tetel.html', {'form': form})

@login_required
def auto_complete(request):
    q = request.GET.get('term', '')
    # users = User.objects.filter(is_active=True)
    users = Artist.objects.filter(Q(name__icontains=q))
    users_list = []

    for u in users:
        value = '%s' % (u.name)
        u_dict = {'id': u.id, 'label': value}
        users_list.append(u_dict)
    data = json.dumps(users_list)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@login_required
def update_tetel(request, slug):
    instance = get_object_or_404(Tetelek, slug=slug)
    fr = TetelekForm(request.POST, instance=instance)
    aid = fr.initial['artist']
    if aid:
        artist_name = Artist.objects.values_list('name', flat=True).get(pk=aid)
    else:
        artist_name = ""
    form = TetelekForm(request.POST or None, initial={'artist': artist_name}, instance=instance)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modified_by = us
        form.save()
        return render(request, 'tetelek_list.html', {})
    return render(request, 'tetelek_update.html', {'form': form})