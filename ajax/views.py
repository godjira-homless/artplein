from django.shortcuts import render
from .forms import AjaxForm
from .models import Ajax


def ajax_list(request):
    items = Ajax.objects.all()
    context = {'items': items}
    return render(request, 'ajax_list.html', context)


def create_ajax(request):
    if request.method == 'POST':
        form = AjaxForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AjaxForm()
    context = {'form': form}
    return render(request, 'ajax_create.html', context)
