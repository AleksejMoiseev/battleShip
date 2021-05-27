from django.urls import path
from .views import *
from django.conf.urls import url


urlpatterns = [
    url(r"^$", test7),
    url(r"^test1/$", test1),
    url(r"^test2/$", test2),
]