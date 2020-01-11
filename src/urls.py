"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('', TemplateView.as_view(template_name='home.html')),
    path('artists/', include('artists.urls')),
    path('appraisers/', include('appraisers.urls')),
    path('technics/', include('technics.urls')),
    path('items/', include('items.urls')),
    path('ajax/', include("ajax.urls")),
    path('project/', include("project.urls")),
    path('lots/', include("lots.urls")),

]
