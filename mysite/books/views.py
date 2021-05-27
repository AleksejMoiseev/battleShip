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
    context = RequestContext(request=request, dict_={}, processors=[custom_context])
    html = template.render(context=context)
    return HttpResponse(html)


def test2(request):
    template = loader.get_template('testbook1.html')
    html = template.render(context=custom_context(request=request))  # функция которая определяет контекст который повторяется
    return HttpResponse(html)
