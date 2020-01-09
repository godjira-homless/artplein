from django.urls import path, include

from . import views


urlpatterns = [

    path('', views.project_list, name='project_list'),
    path('create/', views.create_project, name='create_project'),
    path('champion_auto_complete/', views.champion_auto_complete, name='champion_auto_complete'),

]
