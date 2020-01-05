from django.shortcuts import render
from .models import Item
from .forms import ItemForm

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
