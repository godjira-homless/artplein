from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from .models import Appraisers


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
