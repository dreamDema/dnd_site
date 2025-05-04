from django.db import models
from django.utils.text import slugify
from transliterate import translit




class Adventures(models.Model):

    STATUS_CHOICES = [
        ('Отсутствует', 'Отсутствует'),
        ('Готово', 'Готово'),
        ('В разработке', 'В разработке'),
    ]

    GENRE_CHOICES = [
        ('Не определён', 'Не определён'),
        ('Классическое фэнтези', 'Классическое фэнтези'),
        ('Хоррор', 'Хоррор'),
        ('Детектив', 'Детектив'),
        ('Комедия', 'Комедия'),
    ]

    TYPE_ADVENTURE_CHOICES = [
        ('Ваншот', 'Ваншот'),
        ('Мини приключение', 'Мини приключение'),
        ('Приключение', 'Приключение'),
    ]

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='adventures_images/', blank=True, null=True)
    content = models.TextField(blank=True)
    level = models.CharField(max_length=10, blank=True)
    type_adventure = models.CharField(max_length=20, choices=TYPE_ADVENTURE_CHOICES, default='Ваншот')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Отсутствует')
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='Не определён')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Генерация slug из name перед сохранением
        if not self.slug:
            # Преобразуем имя в латиницу
            slug_name = translit(self.name, 'ru', reversed=True)
            self.slug = slugify(slug_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name