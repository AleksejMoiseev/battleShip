# Generated by Django 3.2 on 2021-06-12 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210527_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessByToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.SmallIntegerField(choices=[(1, 'active'), (0, 'rotten')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.publisher')),
            ],
        ),
    ]
