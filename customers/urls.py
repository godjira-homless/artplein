from django.conf.urls import url
from django.urls import path

from customers import views
from .views import SearchResultsView, edit

urlpatterns = [
    path('', views.index, name='index'),
    path('home.html', views.index, name='home'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('snippet', views.person_detail),
    path('snippet/<int:id>/', views.edit),
]