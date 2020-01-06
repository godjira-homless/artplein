import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from artists.models import Artist


def items_list(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'items_list.html', context)


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

    form = ItemForm()
    return render(request, 'items_create.html', {'form': form})


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
