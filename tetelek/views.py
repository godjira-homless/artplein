import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from extra.models import Extras
from .models import Tetelek, Artist
from .forms import TetelekForm


@login_required
def tetelek_list_old(request):
    tetelek = Tetelek.objects.all()
    context = {'items': tetelek}
    return render(request, 'tetelek_list.html', context)


@login_required
def create_tetelek(request):
    form = TetelekForm(request.POST or None, request.FILES)
    # files = request.FILES.getlist('photo')
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.created_by = us
        form.save()
        return HttpResponseRedirect(reverse('tetelek_list'))
    if Tetelek.objects.exists():
        next_code = Tetelek.objects.last_code()
        next_code.code += 1
    else:
        next_code = 1
    if Extras.objects.filter(owner=request.user).exists():
        extra_artist = Extras.objects.filter(owner=request.user).values_list('artist', flat=True)
        aid = extra_artist[0]
        artist_name = Artist.objects.values_list('name', flat=True).get(pk=aid)
    else:
        artist_name = ""
    form = TetelekForm(initial={'code': next_code, 'artist': artist_name})
    # form = TetelekForm()
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
    fr = TetelekForm(request.POST or None, request.FILES or None, instance=instance)
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
        if request.FILES:
            obj.photo = request.FILES['photo']
        form.save()
        return HttpResponseRedirect(reverse('tetelek_list'))
    return render(request, 'tetelek_update.html', {'form': form})


def tetelek_list(request):
    queryset_list = Tetelek.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) | Q(code__icontains=query)
        )
    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        queryset_list = paginator.page(1)
    except EmptyPage:
        queryset_list = paginator.page(paginator.num_pages)

    context = {'items': queryset_list}
    return render(request, 'tetelek_list.html', context)
