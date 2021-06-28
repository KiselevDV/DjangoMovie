"""
Логика приложения. Функции или классы, которые принимают веб запросы и возращают
ответ (HTML, перенаправление, ошибка ...)
"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


# class MovieView(View):
#     """Список фильмов. Через общий класс View"""
#
#     def get(self, request):
#         """
#         Принимает GET запросы HTTP, request - вся
#         информация с клиента/браузера/фронта
#         """
#         movies = Movie.objects.all()
#         return render(request, 'movies/movie_list.html', {'movie_list': movies})

class MovieView(ListView):
    """Список фильмов. Через специализированный класс ListView"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


# class MovieDetailView(View):
#     """Полное описание фильма. Через общий класс View"""
#
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', {'movie': movie})

class MovieDetailView(DetailView):
    """Полное описание фильма. Через специализированный класс DetailView"""
    model = Movie
    slug_field = 'url'  # поле для поиска записи
