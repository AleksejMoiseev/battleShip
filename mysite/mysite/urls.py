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
from django.urls import include



urlpatterns = [
    url(r"^test1/(\w*)/$", test1),
    url(r"^test21/$", test2),
    path('admin/', admin.site.urls),
    path('test2/', test2, name='django_registration_activation_immediately'),
    path('test3/', test3),
    path('new/', include('books.urls')), #  include помогает подключить все пути находящиеся в другом предсьавлении
    path('test4/', test4),
    path('test5/', test5),
    path('test6/', test6),
    path('test7/', test7),
    path('test8/', test8),
    path('test9/', test9),
    path('test10/', test10),
    url(r"^test12/$", test12, {'template_name': "test12.html"}),
    path('test13/', test12, {'template_name': "test13.html"}),
    path('test2/<int:pk>/', offset),
    url(r'^test14/(?P<order>\[order]*)/', test14),
    url(r'^test15/', test15),

    # url(r"^test11/(\d*)/(\d*)/$", test11), # Передача в функцию позиционных аргументов
]

urlpatterns += [
    url(r"^test11/(?P<year>\d*)/(?P<month>\d*)/$", test11), # передача в функцию именованных аргументов  year, month
]

