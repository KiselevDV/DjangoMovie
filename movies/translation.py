"""
Файл с указанием полей моделей, для которых будет осуществляться перевод

python manage.py update_translation_fields - обновление уже созданных моделей
"""
from modeltranslation.translator import register, TranslationOptions

from .models import Category, Actor, Genre, Movie, MovieShots


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'country')


@register(MovieShots)
class MovieShotsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
