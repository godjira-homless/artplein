import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Tetelek, Artist
from .forms import TetelekForm

@login_required
def tetelek_list(request):
    tetelek = Tetelek.objects.all()
    context = {'items': tetelek}
    return render(request, 'tetelek_list.html', context)

@login_required
def create_tetelek(request):
    form = TetelekForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = TetelekForm()
    return render(request, 'create_tetel.html', {'form': form})

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