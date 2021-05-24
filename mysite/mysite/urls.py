"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r"^test1/(\w*)/$", test1),
    url(r"^test21/$", test2),
    path('admin/', admin.site.urls),
    path('test2/', test2, name='django_registration_activation_immediately'),
    path('test3/', test3),
    path('test4/', test4),
    path('test5/', test5),
    path('test6/', test6),
    path('test7/', test7),
    path('test2/<int:pk>/', offset),
]

