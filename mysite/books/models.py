from django.db import models
from django.db.models import Model
from django.db.models import Q  # импорт Q для составляния сложных запросов
from django.db import connection

# Create your models here.


class ManagerPublisher(models.Manager):

    def my_all(self, name):
        return self.filter(name=name)  # Позволяет создавать новые методы для обращения к базе данных через objects


    def my_method(self):  # Полностью пишем запрос в БД  на основании SQL
        """
        Результат выполнения функции выдает список данных сами формируем QVERY !!!
        [(1, ''Apress'', '2855 Telegraph Avenue', 'Berkeley', 'CA', 'http://www.apress.com/', 'U.S.A.'),
        (2, 'dany', '2855 Telegraph Avenue', 'Moucow', 'CA', 'http://www.apress.com/', 'U.S.A.'),
        (3, 'Aleksei', 'Mouscou', 'Mouscou', 'Mouscou', 'http://127.0.0.1:1111/admin/books/publisher/add/', 'Mouscou')]

        :return:
        """
        cursor = connection.cursor()
        cursor.execute("""
        select * from books_publisher
        """)
        row = cursor.fetchall()
        return row


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')  # Параметр   verbose_name='Имя' позволяет менять
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60, )
    state_province = models.CharField(max_length=30, blank=True)  # Сообщает модели, что поле может быть NULL
    country = models.CharField(max_length=50, null=True)  # Сообщает модели, что поле может быть NULL
    website = models.URLField()
    objects = ManagerPublisher()  # регистрация нового класса расширяющего методы objects

    def __unicode__(self):
        return self.name

    def __str__(self):
        return f"{self.name}" # Задает  str  репрезентацию непосредственно в модели

    class Meta:  # Позволяет добавлять параметры при обращении к моделиз1
        ordering = ['name']
        get_latest_by = ['name']   # Метод latest(field_name=None) определяет по какой записи определяют позднюю запись для вывода


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}


class AccessByToken(models.Model):

    ACTIVE = 1
    NOT_ACTIVE = 0

    IS_ROTTEN = [
        (ACTIVE, "active"),
        (NOT_ACTIVE, 'rotten')
    ]

    user = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    is_active = models.SmallIntegerField( choices=IS_ROTTEN, default=NOT_ACTIVE, verbose_name="Состояние")
