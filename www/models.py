import uuid
import os
from datetime import date

from django.db import models
from django.utils.deconstruct import deconstructible
from django.urls import reverse

from slugify import slugify_ru

from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor


@deconstructible
class ChangeName(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        return os.path.join(self.path + str(instance.film.id), filename)

image_file_name = ChangeName('pictures/')





class Category(models.Model):

    # Категории

    name = models.CharField('Категория', max_length=100)
    description = models.TextField('Описание', blank=True)
    slug = models.SlugField(max_length=100, editable=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_ru(self.name, to_lower=True, max_length=100)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):

    # Жанры

    name = models.CharField('Жанр', max_length=100)
    description = models.TextField('Описание', blank=True)
    slug = models.SlugField(max_length=100, editable=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_ru(self.name, to_lower=True, max_length=100)
        super(Genre, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Cinematographer(models.Model):

    # Актеры, режиссеры, сценаристы, операторы ...

    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание', blank=True)
    image = fields.ImageField('Фото', upload_to='cinematographer/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры, режиссеры, сценаристы, ...'
        verbose_name_plural = 'Актеры, режиссеры, сценаристы, ...'


class Film(models.Model):

    # Фильм

    title = models.CharField(
        'Название фильма',
        max_length=100,
        db_index=True
        )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    date = models.DateField(
        'Дата выхода в прокат',
        default=date.today
        )
    country = models.CharField(
        'Страна',
        max_length=100,
        blank=True
        )
    producers = models.ManyToManyField(
        Cinematographer,
        verbose_name='Продюсер',
        related_name='film_producer',
        blank=True
        )
    directors = models.ManyToManyField(
        Cinematographer,
        verbose_name='Режиссеры',
        related_name='film_director',
        blank=True
        )
    screenwriters = models.ManyToManyField(
        Cinematographer,
        verbose_name='Сценарий',
        related_name='film_screenwriter',
        blank=True
        )
    actors = models.ManyToManyField(
        Cinematographer,
        verbose_name='Актеры',
        related_name='film_actor',
        blank=True
        )
    operators = models.ManyToManyField(
        Cinematographer,
        verbose_name='Операторы',
        related_name='film_operator',
        blank=True
        )
    composers = models.ManyToManyField(
        Cinematographer,
        verbose_name='Композиторы',
        related_name='film_composer',
        blank=True
        )
    genres = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='film_genre',
        blank=True
        )
    budget = models.PositiveIntegerField(
        'Бюджет',
        default=0,
        help_text='сумма в USD'
        )
    age = models.PositiveIntegerField(
        'Возраст',
        default=0,
        )
    time = models.CharField(
        'Длительность',
        max_length=30,
        blank=True
        )
    slug = models.SlugField(
        max_length=100,
        editable=True,
        blank=True
        )
    poster = fields.ImageField(
        'Афиша',
        upload_to='posters/',
        blank=True,
        )
    flag_poster = models.BooleanField(
        'Показывать в афише',
        default=False,
        editable=True
        )
    description = models.TextField(
        'Сюжет',
        blank=True
        )
    trailer_url = models.TextField(
        'URL Видео',
        blank=True
        )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_ru(self.title, to_lower=True, max_length=100)
        super(Film, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('film_details', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class FilmPicture(models.Model):
    film = models.ForeignKey(
        Film,
        verbose_name='Фильм',
        on_delete=models.CASCADE)
    image = fields.ImageField(
        'Изображение',
        upload_to=image_file_name
        )
    image_title = models.CharField(
        'Название изображения',
        max_length=100,
        )
    alt = models.CharField(
        'Alt',
        max_length=100,
        blank=True,
        )
    
    def __str__(self):
        return self.image_title

    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'
