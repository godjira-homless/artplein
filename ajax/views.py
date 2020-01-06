from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import AjaxForm
from .models import Ajax
import json


def ajax_list(request):
    items = Ajax.objects.all()
    context = {'items': items}
    return render(request, 'ajax_list.html', context)


def create_ajax_old(request):
    if request.method == 'POST':
        form = AjaxForm(request.POST)
        if form.is_valid():
            form.save()

    form = AjaxForm()
    return render(request, 'ajax_create.html', {'form': form})


def create_ajax(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Ajax(title=post_text)
        post.save()

        response_data['title'] = post.text

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
