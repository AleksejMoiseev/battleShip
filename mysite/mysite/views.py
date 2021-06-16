import datetime
import os

from django.http import *
from django.shortcuts import render
from django.template import Template, Context, loader
from django.template.loader import render_to_string
from django.urls import reverse

from .form import MyForm

T =os.path.dirname(__file__)  # показывает путь to parent directory

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
        return HttpResponseBadRequest

    context = {
        'current_date': now,
    }
    html_template = template.render(context=context)
    return HttpResponse(html_template)


def test3(request):
    template = 'template2.html'
    context = {'current_date': T}
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
    # return HttpResponse(html)

    # return HttpResponse("Необходимо авторизоваться",  status=401)
    # raise Http404("No MyModel matches the given query.")
    return render(request=request, template_name='error_404.html', status=404)


def test8(request):
    current_date = request.GET
    context = {
        'current_date': request.GET,
    }
    template_name = 'form.html'
    # return render(request=request, template_name=template_name, context=locals())
    # return HttpResponse("<h1 style='color:red'>Я Могу вывести Что угодно</h1>")
    t = loader.get_template(template_name=template_name)  # загрузка кода шаблона и возврат класса TEMPLATE
    html = t.render(context=context)  #  Прокидывание контекста
    return HttpResponse(html)


def test9(request):
    current_date = request.POST  # получаем словарь содержащий в себе данные отправленные пользователем
    template_name = 'form1.html'
    return render(request=request, template_name=template_name, context=locals())


def test10(request):  # использование класса формы для отображения формы
    template_name = 'form2.html'
    data = dict()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # метод cleaned_data позволяет получить данные из формы в виде словаря {}
            # time.sleep(3)
            # return redirect(to='django_registration_activation_immediately')
    else:
        form = MyForm(initial={'message': 'Введите сюда чего нибудь!'})  # Позволяет сюда ывводить данные которые будут показаны при первом вызове

    context = {
        'form': form,
        'my_value': data
    }
    return render(request=request, template_name=template_name, context=context)


def test11(request, year, month):
    template_name = 'test11.html'
    year = year
    month = month
    test = 'Value'
    return render(request=request, template_name=template_name, context=locals(), status=201)


def test12(request, template_name):
    data = 'This is value'
    return render(request=request, template_name=template_name, context=locals(), status=201)


def test14(request, order):
    print(order)
    return HttpResponse(f'oreder; {order}', status=200)


def test15(request):
    t = Template("<html><body><h1>{{name}} </h1> </body></html>")
    context = Context({
        "name": "Alex",
    })
    html = t.render(context=context)
    return HttpResponse(html, status=200)

    # return HttpResponse("Необходимо авторизоваться",  status=401)


