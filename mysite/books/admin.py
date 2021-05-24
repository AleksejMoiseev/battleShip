from django.contrib import admin
from books.models import Publisher


# Register your models here.

@admin.register(Publisher)  # регитстрация через декоратор
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', )  # Добавляет поля  в admin панеле
    search_fields = ('name', )  # добавляет поле для поиска по 'name'
    list_filter = ('country', )  # добавляет фильтр с правой стороны панели для быстрого фильтра по значению
    ordering = ('-name', )  # параметр отвечающий за сортировку
    # filter_horizontal = ('address', ) # Сложный фильтр для связей многие для многих
    # raw_id_fields = ('name', )  # Сложный фильтр для поля Forenkey



# admin.site.register(Publisher)  # Регистрация модели в админ панеле

