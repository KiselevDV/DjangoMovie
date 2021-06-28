"""
Url-ы уровня приложения
"""

from django.urls import path

from .views import (MovieView, MovieDetailView, )

app_name = 'movies'
urlpatterns = [
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('', MovieView.as_view(), name='head_page')
]
