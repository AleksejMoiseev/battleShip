# Generated by Django 3.2 on 2021-06-14 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_accessbytoken_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ByToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_key', models.CharField(max_length=50)),
                ('is_active', models.SmallIntegerField(choices=[(1, 'active'), (0, 'rotten')], default=0, verbose_name='Состояние')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.publisher')),
            ],
        ),
    ]
