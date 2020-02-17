from django.http import request, HttpResponse
from django.shortcuts import render
from .models import Imguploads
from .forms import ImgupForm


def imgup_list(request):
    tetelek = Imguploads.objects.all()
    context = {'items': tetelek}
    return render(request, 'img_list.html', context)


def create_imgup(request):
    form = ImgupForm(request.POST or None, request.FILES)
    if form.is_valid():
        title = form.cleaned_data['title']
        for f in request.FILES.getlist('file'):
            form.file = f
        # return HttpResponse('OK')
        form.save()
    form = ImgupForm()
    return render(request, 'create_img.html', {'form': form})
