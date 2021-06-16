from django.contrib import admin


# Register your models here.
from books.models import *



@admin.register(Publisher)  # регитстрация через декоратор
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', )  # Добавляет поля  в admin панеле
    search_fields = ('name', )  # добавляет поле для поиска по 'name'
    list_filter = ('country', )  # добавляет фильтр с правой стороны панели для быстрого фильтра по значению
    ordering = ('-name', )  # параметр отвечающий за сортировку
    # filter_horizontal = ('address', ) # Сложный фильтр для связей многие для многих
    # raw_id_fields = ('name', )  # Сложный фильтр для поля Forenkey


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('year_in_school',)
# admin.site.register(Publisher)  # Регистрация модели в админ панеле

@admin.register(AccessByToken)
class AccessByTokenAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'user')

@admin.register(ByToken)
class AccessByTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token_key', 'is_active', 'date_of_creation', 'update_date')

