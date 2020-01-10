from django.urls import path

from . import views


urlpatterns = [

    path('', views.lots_list, name='lots_list'),
    path('create/', views.create_lot, name='create_lot'),
    #path('contact-name-search/', views.contact_name_search, name='contact-name-search'),

]
