from django.urls import path

from . import views


urlpatterns = [
    # path('', views.technics, name='technics'),
    #path('<slug:slug>', TechnicDetailView.as_view(), name='technic_detail'),
    path('', views.items_list, name='items_list'),
    #path('<slug:slug>/delete/', TechnicDeleteView.as_view(), name='technic_delete'),
    path('create/', views.create_item, name='item_create'),
    #path('<slug:slug>/update/', TechnicUpdateView.as_view(), name='technic_update'),
]
