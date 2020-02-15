from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Extras
from .forms import ExtrasForm


@login_required
def extra_list(request):
    extra = Extras.objects.all()
    context = {'items': extra}
    return render(request, 'extra_list.html', context)


@login_required
def create_extra(request):
    form = ExtrasForm(request.POST or None)
    current_user_added = Extras.objects.filter(owner=request.user).exists()
    if current_user_added:
        return HttpResponseRedirect(reverse('extra_list'))
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.owner = us
        form.save()
        return HttpResponseRedirect(reverse('extra_list'))
    form = ExtrasForm()
    return render(request, 'extra_create.html', {'form': form})