from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Tetelek
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