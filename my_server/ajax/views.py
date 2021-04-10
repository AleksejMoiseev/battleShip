from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


from ajax.forms import CreateUserForm
from ajax.serializers import *
from ajax.models import Game, User
from rest_framework.permissions import AllowAny
from django.views.generic import CreateView

from django.conf import settings

# Create your views here.


def myfunc(request):
    return HttpResponse("<h1>Privet</h1>")


class GameCreateView(generics.ListCreateAPIView):
    serializer_class = GameDetailSerializers
    queryset = Game.objects.all()


class UserCreateView(generics.ListCreateAPIView):
    serializer_class = UserListSerializers
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        # request.set_cookie(key='id', value=38)
        print(request.user)
        print(request.session)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        id_user = serializer.data['id']
        request.session['id'] = id_user
        print(request.session)
        print(request.session['id'])
        headers['id'] = id_user
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        response.set_cookie(key='id', value=id_user)
        return response


class GameRetriveView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameDetailSerializers
    queryset = Game.objects.all()
    lookup_field = 'id'
    permission_classes = (AllowAny, )

"""
Еще одна реализация через написания логики в самом классе через наследования базового класса APIView,  и 
самостоятельному определению метода get
"""


class GameDetailView(APIView):

    def get(self, request, id):
        game = Game.objects.get(id=id)  # выбираем из базы данных   query данные с id=id
        serializer = GameDetailSerializers(game)  # устанавливаем сериализатор
        return Response(serializer.data)  # Возвращаем Responce c данными


class UserDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = UserListSerializers
    queryset = User.objects.all()


def assign_const(request):
    settings.MY_CONST = 2222
    print(settings.MY_CONST)
    return HttpResponse(settings.MY_CONST)

def view_const(request):
    from django.conf import settings
    print(settings.MY_CONST)
    return HttpResponse(settings.MY_CONST)


# class CreateUserAndGame(CreateView):
#     form_class = CreateUserForm
#     template_name = "my_server/fronted/auth.html"
#     context_object_name = 'name_user'
#
#

class CreateUserAndGame(generics.CreateAPIView):
    serializer_class = CreateStartGame
    queryset = Game.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data['name']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        id_game = serializer.data['id']
        game = Game.objects.get(id=id_game)
        created_user = User.objects.create(name=name, game=game)
        headers = self.get_success_headers(serializer.data)
        headers['id_user'] = created_user.pk
        response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        response.set_cookie(key='id', value=created_user.pk)
        return response


class UpdateShip(generics.RetrieveUpdateAPIView):
    serializer_class = UserShipStatusUpdate
    queryset = User.objects.all()


def faire(request):
    print(request.user)
    print(request.data['coordinate'])
    response = HttpResponse(content="privet")
    return response










