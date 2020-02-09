from django.urls import path
from . import views

urlpatterns = [

    path('', views.tetelek_list, name='tetelek_list'),
    path('create/', views.create_tetelek, name='create_tetelek'),
    path('update/<slug:slug>', views.update_tetel, name='update_tetel'),
    # path('<slug:slug>', views.detail_lot, name='detail_lot'),
    path('auto_complete/', views.auto_complete, name='auto_complete'),

]

