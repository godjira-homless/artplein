from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Lots
from artists.models import Artist
from .forms import LotsForm
import json


def lots_list(request):
    lots = Lots.objects.all()
    context = {'items': lots}
    return render(request, 'lots_list.html', context)


def create_lot(request):
    if request.method == 'POST':
        form = LotsForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.save()
    form = LotsForm()
    return render(request, 'create_lots.html', {'form': form})


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
