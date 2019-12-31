from django.urls import path
from appraisers import views


urlpatterns = [
    path('', views.appraisers, name='appraisers'),
    path('new_appraiser', views.new_appraiser, name='new_appraiser'),

]