from django.urls import path

from . import views


urlpatterns = [

    path('', views.tetelek_list, name='tetelek_list'),
    path('create/', views.create_tetelek, name='create_tetelek'),
    #path('update/<slug:slug>', views.update_lot, name='update_lot'),
    #path('<slug:slug>', views.detail_lot, name='detail_lot'),
    #path('artist_auto_complete/', views.artist_auto_complete, name='artist_auto_complete'),

]