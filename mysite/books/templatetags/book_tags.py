from django.template import defaulttags, defaultfilters
from django import template
register = template.Library()  # регистрируем библиотеку тэгов
"""
Здесь можно описать любые фильтры, котрые мы хотим применить в своем приложении, далее мы их региструем посредством
декоратора @register.filter и загружаем через {% load book_tags %} в своем шаблоне далее исполуем
<h1>MOй шаблон {{ name|my_tag }}</h1>
"""


@register.filter
def my_tag(value):
    return value.lower()


@register.filter()
def add_host(value):
    return value + "_host"