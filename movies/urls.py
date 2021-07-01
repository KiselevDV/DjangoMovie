"""
Url-ы уровня приложения
"""

from django.urls import path

from .views import (
    MovieView, MovieDetailView, AddReview, ActorDetailView, FilterMoviesView,
    JsonFilterMoviesView, AddStarRating, Search, )

app_name = 'movies'
urlpatterns = [
    # Поиск по фильмам
    path('search/', Search.as_view(), name='search'),

    # Добавление рейтинга
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),

    # Фильтрация по годам и жанрам
    path("filter/", FilterMoviesView.as_view(), name='filter'),
    path("json-filter/", JsonFilterMoviesView.as_view(), name='json_filter'),

    # Отывы к фильму
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),

    # Главная страница, детальные данные о фильмах, актёрах и режиссёрах
    path('actor/<str:slug>', ActorDetailView.as_view(), name='actor_detail'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('', MovieView.as_view(), name='head_page')
]
