from django.urls import path

from . import views


urlpatterns = [

    path('', views.ajax_list, name='ajax_list'),
    path('create/', views.create_ajax, name='create_ajax'),

]
