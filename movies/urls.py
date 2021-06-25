"""
Url-ы уровня приложения
"""

from django.urls import path

from .views import (MovieView, MovieDetailView, )

urlpatterns = [
    path('<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('', MovieView.as_view(), name='head_page')
]
