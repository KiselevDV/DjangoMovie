"""
Темплейт теги для таблицы Movie

Регистрация темплейт тегов осуществляется с помощью метода Library(),
через декораторы: simple_tag и inclusion_tag
register = template.Library() - переменная для регистрации
inclusion_tag - может рендерить шаблон
"""
from django import template

from movies.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    """Вывод последних добавленных записей"""
    movies = Movie.objects.order_by('-id')[:count]  # 5 последних
    return {'last_movies': movies}
