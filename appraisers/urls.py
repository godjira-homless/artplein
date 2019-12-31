from django.urls import path
from appraisers import views


urlpatterns = [
    path('', views.appraisers, name='appraisers'),

]