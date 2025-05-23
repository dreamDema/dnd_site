# Generated by Django 5.2 on 2025-05-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_online', '0004_adventures_genre_adventures_type_adventure_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventures',
            name='level',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='adventures',
            name='type_adventure',
            field=models.CharField(choices=[('oneshote', 'Ваншот'), ('mini_company', 'Мини приключение'), ('company', 'Приключение')], default='oneshot', max_length=15),
        ),
    ]
