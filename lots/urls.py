from django.urls import path

from . import views


urlpatterns = [

    path('', views.lots_list, name='lots_list'),
    path('create/', views.create_lot, name='create_lot'),
    path('update/<slug:slug>', views.update_lot, name='update_lot'),
    path('<slug:slug>', views.detail_lot, name='detail_lot'),
    path('artist_auto_complete/', views.artist_auto_complete, name='artist_auto_complete'),

]
