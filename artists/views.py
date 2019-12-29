from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import Artist


def artists(request):
    return render(request, 'artists.html', {})

def artist_detail(request, id):
    qv = Artist.objects.get(pk=id)
    prev = request.META.get('HTTP_REFERER')
    context = {'id': id, 'name': qv.name, 'bio': qv.bio, 'prev': prev}
    return render(request, 'artist_detail.html', {'context': context})

class ArtistResults(ListView):
    model = Artist
    template_name = 'artists.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q' or None)
        print(query)
        if query:
            object_list = Artist.objects.filter(
                Q(name__icontains=query) | Q(bio__icontains=query)
            )
            return object_list

