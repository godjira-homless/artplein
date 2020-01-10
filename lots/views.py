from django.shortcuts import render


def lots_list(request):
    # items = Ajax.objects.all()
    context = {}
    return render(request, 'lots_list.html', context)


def create_lot(request):
    pass