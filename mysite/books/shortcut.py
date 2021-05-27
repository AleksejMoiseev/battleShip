

def custom_context(request):
    context = {
        'month': "Здесь пишем месяц",
        'year': "Здесь пишем месяц",
        "name": 'alex',
    }
    return context