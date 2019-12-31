from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from .models import Appraisers
from .forms import AppraiserForm


def appraisers(request):
    queryset_list = Appraisers.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query)
        )
    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        queryset_list = paginator.page(1)
    except EmptyPage:
        queryset_list = paginator.page(paginator.num_pages)

    context = {'queryset_list': queryset_list}
    return render(request, 'appraisers.html', context)

def new_appraiser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppraiserForm(request.POST)
        if form.is_valid():
            form.save()
            form = AppraiserForm()
            error_message = "Nincs hiba"
            context = {'form': form, 'error_message': error_message}
            #return render(request, 'appraisers.html', context)
            return redirect(appraisers)

        else:
            error_message = "Hiba van"
            form = AppraiserForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'appraisers.html', context)