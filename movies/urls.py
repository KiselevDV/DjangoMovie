"""
Url-ы уровня приложения
"""

from django.urls import path

from .views import (MovieView, MovieDetailView, AddReview, ActorView, )

app_name = 'movies'
urlpatterns = [
    path('actor/<str:slug>', ActorView.as_view(), name='actor_detail'),
    path('review/<int:pk>', AddReview.as_view(), name='add_review'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('', MovieView.as_view(), name='head_page')
]
