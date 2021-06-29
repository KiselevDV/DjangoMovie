"""
Url-ы уровня приложения
"""

from django.urls import path

from .views import (
    MovieView, MovieDetailView, AddReview, ActorDetailView, FilterMoviesView, )

app_name = 'movies'
urlpatterns = [
    # Фильтрация по фгодам и жанрам
    path("filter/", FilterMoviesView.as_view(), name='filter'),

    # Отывы к фильму
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),

    # Главная страница, детальные данные о фильмах, актёрах и режиссёрах
    path('actor/<str:slug>', ActorDetailView.as_view(), name='actor_detail'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('', MovieView.as_view(), name='head_page')
]
