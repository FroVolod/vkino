# Generated by Django 3.0.7 on 2020-06-23 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20200623_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='poster_jpeg',
        ),
    ]
