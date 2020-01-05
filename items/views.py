from django.shortcuts import render

def items_list(request):

    context = {}
    return render(request, 'items_list.html', context)

def create_item(request):

    context = {}
    return render(request, 'items_create.html', context)
