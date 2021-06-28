"""
Файл для регистрации моделей и их вывода, в административной панеле Django

StackedInline/TabularInline - может работать с m2m и foreignkey
"""
from django.contrib import admin

from .models import (
    Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews)


class ReviewInLines(admin.TabularInline):
    """Отзывы на странице ..."""
    model = Reviews
    extra = 1  # кол-во доп. пустых форм
    readonly_fields = ('name', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актёры и режиссёры"""
    list_display = ('name', 'age')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name', 'url')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')  # имя поля связанной модели
    inlines = (ReviewInLines,)  # встроить связанные таблицы (m2m/foreignkey)
    save_on_top = True
    save_as = True  # сохранить как новый объект (для однотипных ообъектов)
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', 'poster')
        }),
        (None, {
            'fields': (('year', 'world_premiere'), 'country')
        }),
        ('Other', {
            'classes': ('collapse',),  # collapse - скрыть поля
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fess_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('title', 'movie')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('ip', 'movie')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


admin.site.register(RatingStar)
