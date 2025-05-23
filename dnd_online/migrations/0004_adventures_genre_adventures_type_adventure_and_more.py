# Generated by Django 5.2 on 2025-05-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_online', '0003_adventures_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventures',
            name='genre',
            field=models.CharField(choices=[('default', 'Не определён'), ('classic', 'Классическое фэнтези'), ('horror', 'Хоррор'), ('detective', 'Детектив'), ('comedy', 'Комедия')], default='default', max_length=20),
        ),
        migrations.AddField(
            model_name='adventures',
            name='type_adventure',
            field=models.CharField(choices=[('oneshote', 'Ванишот'), ('mini_company', 'Мини приключение'), ('company', 'Приключение')], default='oneshot', max_length=15),
        ),
        migrations.AlterField(
            model_name='adventures',
            name='status',
            field=models.CharField(choices=[('miss', 'Отсутствует'), ('ready', 'Готов для игры'), ('in_progres', 'В разработке')], default='miss', max_length=15),
        ),
    ]
