"""
Логика приложения. Функции или классы, которые принимают веб запросы и
возращают ответ (HTML, перенаправление, ошибка ...)

request - запрос от клиента; response - ответ клиенту
"""
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ReviewForm, RatingForm
from .mixins import GenreYear
from .models import (
    Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews)


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
    paginate_by = 3

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
    queryset = Movie.objects.filter(draft=False)
    slug_field = 'url'  # поле для поиска записи

    def get_context_data(self, **kwargs):
        """Добавляем форму рейтинга, через переменную 'star_form'"""
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['form'] = ReviewForm()
        return context


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
    paginate_by = 3

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
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        """Для корректной работы при пагинации"""
        context = super().get_context_data(*args, **kwargs)
        # Сформируем GET строку из списка request.GET.getlist("year")
        context['year'] = ''.join([
            f'year={x}&' for x in self.request.GET.getlist("year")])
        context['genre'] = ''.join([
            f'genre={x}&' for x in self.request.GET.getlist("genre")])
        return context


class JsonFilterMoviesView(ListView):
    """Фильтр фильмов в JSON (AJAX через fetch и hogan.js)"""

    def get_queryset(self):
        """
        distinct - исключить повторения;
        values - указать поля, которые забираем
        """
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)


class AddStarRating(View):
    """Добавление рейтинга к фильму"""

    def get_client_ip(self, request):
        """Получить ip клиента из request.META"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            # Один клиент, может выставить значение лишь раз - update_or_create
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                # <input type="hidden" value="{{ movie.id }}" name="movie">
                movie_id=int(request.POST.get('movie')),
                # <input type="radio" id="rating{{ v }}" name="star" ...>
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(ListView):
    """Поиск фильмов"""
    paginate_by = 3

    def get_queryset(self):
        # Данные из формы с name='q' (<input type="search" placeholder="
        # Введите название ..." name="q" class="form-control" required="">)
        return Movie.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        """Расширить контекст для пагинации"""
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f"q={self.request.GET.get('q')}&"
        return context


# Доп. уроки. Джанго под капотом
def func(request, *args, **kwargs):  # blabla, pk  # url
    # return HttpResponse('Hi Django', status=200)
    print(kwargs)
    # URL-ы для теста
    print(request.GET)
    # http://127.0.0.1:8000/en/test/django/123456789/?page=33&test=roro&stream=django+http
    # print(request.GET.get('page'))
    # http://127.0.0.1:8000/en/test/django/123456789/?filters=films,movie,genre
    # print(request.GET.get('filters'))
    # http://127.0.0.1:8000/en/test/django/123456789/?filters=films&filters=movie&filters=genre
    print(request.GET.getlist('filters'))
    return render(request, 'base.html', {'title': 'Test H1'})
