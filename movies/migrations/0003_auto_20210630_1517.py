# Generated by Django 3.2.4 on 2021-06-30 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_fess_in_world'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'МедиаФайл', 'verbose_name_plural': 'МедиаФайлы'},
        ),
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ('-value',), 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звёзды рейтинга'},
        ),
    ]
