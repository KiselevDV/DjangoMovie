"""
Файл для регистрации моделей и их вывода, в административной панеле Django

StackedInline/TabularInline - может работать с m2m и foreignkey
mark_safe - вывод кода HTML как тег
"""
from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import MovieAdminForm
from .models import (
    Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews)


class ReviewInLines(admin.TabularInline):
    """Отзывы на странице c ..."""
    model = Reviews
    extra = 1  # кол-во доп. пустых форм
    readonly_fields = ('name', 'email')


class MovieShotsInLines(admin.TabularInline):
    """Кадры из фильма на странице c ..."""
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        """Получение и вывод изображения"""
        return mark_safe(f'<img src={obj.image.url} width="auto" height="190">')

    get_image.short_description = 'Кадр из фильма'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актёры и режиссёры"""
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        """Вывод изображения, obj - объект модели актёров"""
        return mark_safe(f'<img src={obj.image.url} width="auto" height="80">')

    get_image.short_description = 'Аватарка'


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
    readonly_fields = ('get_image',)
    inlines = (MovieShotsInLines, ReviewInLines)  # встроить связанные таблицы (m2m/foreignkey)
    save_on_top = True
    save_as = True  # сохранить как новый объект (для однотипных ообъектов)
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'),)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'))
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
    form = MovieAdminForm  # подключение формы (с ckeditor)

    def get_image(self, obj):
        """Получение и вывод изображения"""
        return mark_safe(f'<img src={obj.poster.url} width="auto" height="120">')

    get_image.short_description = 'Постер'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""
    list_display = ('title', 'movie', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        """Получение и вывод изображения"""
        return mark_safe(f'<img src={obj.image.url} width="auto" height="80">')

    get_image.short_description = 'Кадр из фильма'


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

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'
