# Generated by Django 3.1.7 on 2021-04-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax', '0003_auto_20210403_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
