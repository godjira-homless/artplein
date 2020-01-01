from django.urls import path

from .views import TechnicListView, TechnicDetailView, TechnicDeleteView, TechnicCreateView, TechnicUpdateView

app_name = 'technics'
urlpatterns = [
    # path('', views.technics, name='technics'),
    path('<slug:slug>', TechnicDetailView.as_view(), name='technic_detail'),
    path('', TechnicListView.as_view(), name='technic_list'),
    path('<slug:slug>/delete/', TechnicDeleteView.as_view(), name='technic_delete'),
    path('create/', TechnicCreateView.as_view(), name='technic_create'),
    path('<slug:slug>/update/', TechnicUpdateView.as_view(), name='technic_update'),
]
