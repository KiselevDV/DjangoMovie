"""
Url-ы уровня приложения
"""

from django.urls import path

from .views import (MovieView, MovieDetailView, AddReview, )

app_name = 'movies'
urlpatterns = [
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('', MovieView.as_view(), name='head_page')
]
