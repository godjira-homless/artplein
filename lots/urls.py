from django.urls import path

from . import views


urlpatterns = [

    path('', views.lots_list, name='lots_list'),
    path('create/', views.create_lot, name='create_lot'),
    path('artist_auto_complete/', views.artist_auto_complete, name='artist_auto_complete'),

]
