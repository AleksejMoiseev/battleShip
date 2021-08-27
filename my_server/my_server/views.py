from django.shortcuts import render
from rest_framework import status


def pageNotFound(request, exception):
    return render(request=request, template_name='error_404.html', status=status.HTTP_404_NOT_FOUND)