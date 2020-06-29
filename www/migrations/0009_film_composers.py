# Generated by Django 3.0.7 on 2020-06-29 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0008_auto_20200624_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='composers',
            field=models.ManyToManyField(blank=True, related_name='film_composer', to='www.Cinematographer', verbose_name='Композиторы'),
        ),
    ]
