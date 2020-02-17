from django.urls import path
from . import views

urlpatterns = [

    path('', views.imgup_list, name='imgup_list'),
    path('create/', views.create_imgup, name='create_imgup'),
    # path('update/<slug:slug>', views.update_tetel, name='update_tetel'),
    # path('<slug:slug>', views.detail_lot, name='detail_lot'),
    # path('auto_complete/', views.auto_complete, name='auto_complete'),

]

