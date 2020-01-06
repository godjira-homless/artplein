from itertools import chain

from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from .models import Artist
from .forms import ArtistForm


def artists(request):
    form = ArtistForm()
    return render(request, 'artists.html', {'form': form})


def artist_detail(request, id):
    qv = Artist.objects.get(pk=id)
    prev = request.META.get('HTTP_REFERER')
    context = {'id': id, 'name': qv.name, 'bio': qv.bio, 'prev': prev}
    return render(request, 'artist_detail.html', {'context': context})


class ArtistResults(ListView):
    model = Artist
    form_class = ArtistForm
    template_name = 'artists.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q' or None)
        if query:
            object_list = Artist.objects.filter(
                Q(name__icontains=query) | Q(bio__icontains=query)
            )

            return object_list


def new_artist(request):
    if request.method == 'POST':

        form = ArtistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm()

    return render(request, 'artists.html', {'form': form})


def edit_artist(request, id=None):
    id = get_object_or_404(Artist, pk=id)
    form = ArtistForm(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('artists'))
    return render(request, 'form.html', {'form': form})