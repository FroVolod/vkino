# Generated by Django 3.0.7 on 2020-06-24 14:12

from django.db import migrations, models
import smartfields.fields
import www.models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_remove_film_poster_jpeg'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='trailer',
            field=smartfields.fields.FileField(blank=True, upload_to='trailer/', verbose_name='Видео'),
        ),
        migrations.AlterField(
            model_name='cinematographer',
            name='image',
            field=smartfields.fields.ImageField(blank=True, upload_to='cinematographer/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='filmpicture',
            name='image',
            field=smartfields.fields.ImageField(upload_to=www.models.ChangeName('pictures/'), verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='filmpicture',
            name='image_title',
            field=models.CharField(max_length=100, verbose_name='Название изображения'),
        ),
    ]