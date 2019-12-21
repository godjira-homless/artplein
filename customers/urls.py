from django.urls import path

from customers import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home.html', views.index),
    path('<int:question_id>/', views.detail, name='detail'),
]