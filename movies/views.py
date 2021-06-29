"""
Логика приложения. Функции или классы, которые принимают веб запросы и
возращают ответ (HTML, перенаправление, ошибка ...)
"""
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ReviewForm
from .mixins import GenreYear
from .models import Category, Actor, Movie


# class MovieView(View):
#     """Список фильмов. Через общий класс View"""
#
#     def get(self, request):
#         """
#         Принимает GET запросы HTTP, request - вся
#         информация с клиента/браузера/фронта
#         """
#         movies = Movie.objects.all()
#         return render(request, 'movies/movie_list.html', {
#             'movie_list': movies
#         })

class MovieView(GenreYear, ListView):
    """Список фильмов. Через специализированный класс ListView"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)

    # def get_context_data(self, *args, **kwargs):
    #     """Расширяем context категориями"""
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


# class MovieDetailView(View):
#     """Полное описание фильма. Через общий класс View"""
#
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', {'movie': movie})

class MovieDetailView(GenreYear, DetailView):
    """Полное описание фильма. Через специализированный класс DetailView"""
    model = Movie
    slug_field = 'url'  # поле для поиска записи


class ActorDetailView(GenreYear, DetailView):
    """Вывод информации о актёре"""
    model = Actor
    slug_field = 'name'
    template_name = 'movies/actor.html'


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)

            # Для ответа на отзыв
            # (в отправленной форме ищем ключ - name='parent')
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))

            # Указывем фильм для данной формы (через его id).
            # 'movie' - поле из таблицы Review + '_id' т.к. (ForeignKey)
            # form.movie_id = pk
            form.movie = movie  # то же, через присвоение самого объекта
            form.save()

        return redirect(movie.get_absolute_url())


class FilterMoviesView(GenreYear, ListView):
    """Фильтр фильмов"""

    def get_queryset(self):
        """
        Получить все фильмы, где года (year) будут входить (__in)
        в список годов (getlist('year')) с фронта (request.GET).
        То же для жанров. getlist - получить данные в виде листа.
        """
        # Получить кверисет с логическим 'И'
        # queryset = Movie.objects.filter(
        #     year__in=self.request.GET.getlist('year'),
        #     genres__in=self.request.GET.getlist('genre'),
        # )
        # Получить кверисет с логическим 'ИЛИ' с помощью Q
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genre'))
        )
        return queryset
