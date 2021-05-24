from django.db import models
from django.db.models import Model
from django.db.models import Q  # импорт Q для составляния сложных запросов

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')  # Параметр   verbose_name='Имя' позволяет менять
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30, blank=True)  # Сообщает модели, что поле может быть NULL
    country = models.CharField(max_length=50, null=True)  # Сообщает модели, что поле может быть NULL
    website = models.URLField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return f"{self.name}" # Задает  str  репрезентацию непосредственно в модели

    class Meta:  # Позволяет добавлять параметры при обращении к моделиз1
        ordering = ['name']
        get_latest_by = ['name']   # Метод latest(field_name=None) определяет по какой записи определяют позднюю запись для вывода