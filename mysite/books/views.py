from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, RequestContext, loader
from django.template.loaders.filesystem import Loader

# Create your views here.
from .shortcut import custom_context


def test7(request):
    t = Template("<html><body><h1>{{name|default:'Это строковый литерал.'}} </h1> </body></html>")
    # |default:'Это строковый литерал.' устанавливает значение по умолчанию
    context = Context({
        "name": "alert('Alex')",
    })
    html = t.render(context=context)
    return HttpResponse(html)


def test1(request):
    template = Template('{{ year }}: {{ month }}')
    # t = Loader.get_template(template_name='test11.html') не разобрался с загрузчиками
    context = RequestContext(request=request, dict_={}, processors=[custom_context]) #Позволяет прокинуть кастомный контекст
    html = template.render(context=context)
    return HttpResponse(html)


def test2(request):
    template = loader.get_template('testbook1.html')
    html = template.render(context=custom_context(request=request))  # функция которая определяет контекст который повторяется
    return HttpResponse(html)


def test3(request):
    template = loader.get_template('csrf.html')
    csrftoken = request.COOKIES['csrftoken']  # Получение кук по ключу csrftoken
    sessionid = request.COOKIES['sessionid']   # Получение кук по ключу и ссесии
    html = template.render(context=locals())  # функция которая определяет контекст который повторяется
    responce = HttpResponse(html)
    responce.set_cookie(key='id', value=3, max_age=3)
    # Установка кук в респонс  результат в браузере Set-Cookie: id=3; Path=/, -
    """
   max_age  Время хранения cookie в секундах. Если параметр
            равен None, то cookie будет храниться до момента
            закрытия броузера.
    """
    print(request.session)
    return responce


def hello_world(request):
    return HttpResponse('<h1 style = "color:red">Hello World</h1>')