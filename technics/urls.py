from django.urls import path

from .views import TechnicListView, TechnicDetailView


urlpatterns = [
    #path('', views.technics, name='technics'),
    path('<slug:slug>', TechnicDetailView.as_view(), name='technic_detail'),
    path('', TechnicListView.as_view(), name='technic_list')

]