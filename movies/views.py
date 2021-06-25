"""
Логика приложения. Функции или классы, которые принимают веб запросы и возращают
ответ (HTML, перенаправление, ошибка ...)
"""
from django.shortcuts import render
from django.views import View

from .models import Movie


class MovieView(View):
    """Список фильмов"""

    def get(self, request):
        """
        Принимает GET запросы HTTP, request - вся
        информация с клиента/браузера/фронта
        """
        movies = Movie.objects.all()
        return render(request, 'movies/movies.html', {'movie_list': movies})


class MovieDetailView(View):
    """Полное описание фильма"""

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        return render(request, 'movies/movie_detail.html', {'movie': movie})
