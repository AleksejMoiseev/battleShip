
# Создаем кастомный контекст который можем прокидывать = RequestContext(request=request, dict_={}, processors=[custom_context])
def custom_context(request):
    context = {
        'month': "Здесь пишем месяц",
        'year': "Здесь пишем месяц",
        "name": 'alex',
    }
    return context