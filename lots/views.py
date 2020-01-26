from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Lots
from artists.models import Artist
from .forms import LotsForm
import json

@login_required
def lots_list(request):
    lots = Lots.objects.all()
    context = {'items': lots}
    return render(request, 'lots_list.html', context)


@login_required
def create_lot(request):
    form = LotsForm(request.POST or None)
    """
    if request.method == 'POST':
        aid = request.POST.get("artist")
        # artist_name = Artist.objects.get(pk=aid)
        try:
            artist_name = Artist.objaid = request.POST.get("artist")ects.get(pk=aid)
        except Artist.DoesNotExist:
            artist_name = None
    """
    aid = request.POST.get("artist")
    if aid:
        print(aid)
        aname = request.POST.get("artist_display")
        form.artist, created = Artist.objects.get_or_create(name=aname)

    if form.is_valid():
        aname = form.cleaned_data['artist']
        us = request.user
        obj = form.save(commit=False)
        obj.created_by = us
        if aname:
            obj.artist, created = Artist.objects.get_or_create(name=aname)
        form.save()
    form = LotsForm()
    return render(request, 'create_lots.html', {'form': form})

@login_required
def update_lot(request, slug):
    instance = get_object_or_404(Lots, slug=slug)
    form = LotsForm(request.POST or None, instance=instance, initial={'artist_display': instance.artist})
    # form = LotsForm(initial={'artist_display': ar}, instance=instance)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modified_by = us
        form.save()
        return render(request, 'lots_list.html', {})
    return render(request, 'lots_update.html', {'form': form})


@login_required
def artist_auto_complete(request):
    q = request.GET.get('term', '')
    # users = User.objects.filter(is_active=True)
    users = Artist.objects.filter(Q(name__icontains=q) | Q(bio__icontains=q))
    users_list = []

    for u in users:
        value = '%s, %s' % (u.name, u.bio)
        u_dict = {'id': u.id, 'label': value, 'value': value}
        users_list.append(u_dict)
    data = json.dumps(users_list)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@login_required
def detail_lot(request, slug):
    q = Lots.objects.filter(slug__iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {
        'post': q,
    }
    return render(request, 'lot_detail.html', context)
