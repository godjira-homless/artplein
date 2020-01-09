from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import json
from .forms import Project, ProjectForm


def project_list(request):
    pass


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.save()
    form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})


def champion_auto_complete(request):
    q = request.GET.get('term', '')
    users = User.objects.filter(is_active=True)
    users_list = []

    for u in users:
        value = '%s, %s (%s) - %s' % (u.last_name, u.first_name, u.username, u.email)
        u_dict = {'id': u.id, 'label': value, 'value': value}
        users_list.append(u_dict)
    data = json.dumps(users_list)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

