import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy, reverse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
import os


T =os.path.dirname(__file__)

# Через хост прокидываем параметр в функцию параметр a: http://example.com:9000/test1/5/


def test1(request, a):
    now = datetime.datetime.now()
    print(a)  # Прокидывается в формате str
    html_template = "<html><body><h1>Сейчас %s Прокинули через хост значение %s </h1> </body></html>" % (now, a)
    return HttpResponse(html_template)


def offset(request, pk):
    html_template = "<html><body><h1>offset %s</h1> </body></html>" % pk
    return HttpResponse(html_template)


def test2(request):
    template_str = 'template2.html'
    now = datetime.datetime.now()
    try:
        template = loader.get_template(template_name=template_str)
    except loader.TemplateDoesNotExist:
        print('ничего нет')

    context = {
        'current_date': now,
    }
    html_template = template.render(context=context)
    return HttpResponse(html_template)


def test3(request):
    template = 'template2.html'
    context = {'current_date': 'http://I am go to walk Mouscow'}
    return render(request=request, template_name=template, context=context, status=200)


def test4(request):
    template = 'template2.html'
    current_date = datetime.datetime.now()
    context = {
        'EMAIL_SUBJECT_PREFIX': "БЛИН КЛИНТОН",
    }
    rendered = render_to_string(template_name='activation_user_subject.txt', context=context)
    current_first = rendered
    athlete_list = ['qqqqqq', "wwwwwwwww", "eeeeeeee"]  # работа с тэгами
    return render(request=request, template_name=template, context=locals(), status=200)


def test5(request):
    template = 'test.html'
    current_date = datetime.datetime.now()
    current_first = 'Еще одна переменная'
    path = request.path  # показывает путь /test5/
    get_host = request.get_host()  # показывает domain 127.0.0.1:1111
    get_full_path = request.get_full_path()  # Путь path вместe со строкой запросa (если присутствует)
    if request.is_secure():
        is_secure = "TRUE"
    else:                                      #True, если запрос отправлен по протоколу HTTPS, иначе False
        is_secure = "FALSE"
    META = request.META                      #  это словарь Python, содержащий все HTTP-заголовки данного запроса
    return render(request=request, template_name=template, context=locals(), status=200)



def test6(request):
    template = 'test.html'
    current_date = datetime.datetime.now()
    current_first = 'Еще одна переменная'
    return HttpResponseRedirect(reverse('django_registration_activation_immediately'))  # Редиректит на на url
                                                                 # c name = 'django_registration_activation_immediately'

    # return HttpResponseRedirect (reverse(test2))  # редиректит на  views c именем test2
    # return redirect(to='/test21/')  # редирект на путь '/test21/'


def test7(request):
    t = Template("<html><body><h1>{{name}} </h1> </body></html>")
    context = Context({
        "name": "Alex",
    })
    html = t.render(context=context)
    return HttpResponse(html)