from django.urls import path

from . import views
from ajax.views import create_ajax


urlpatterns = [

    path('', views.ajax_list, name='ajax_list'),
    path('create/', views.create_ajax, name='create_ajax'),

]
