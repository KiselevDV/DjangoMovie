"""
Формы
"""
from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

# from ckeditor.widgets import CKEditorWidget
# Виджет для загрузки фалов - ckeditor_uploader
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Movie, Rating, RatingStar, Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text', 'captcha')
        # Для корректного рендера (сохранения стилей) при reCaptcha,
        # т.к. форма просто теги в HTML
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border'}),
            'text': forms.Textarea(attrs={'class': 'form-control border'}),
        }


class MovieAdminForm(forms.ModelForm):
    """
    Форма для модели Movie, с кастомным виджетом из 'ckeditor',
    для поля описания фильма (movie.description)
    """
    # Переопределяем стандартное поле
    # description = forms.CharField(
    #     label='Описание', widget=CKEditorUploadingWidget())
    # Для мультиязычного сайта
    description_ru = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget())
    description_en = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None,
    )

    class Meta:
        model = Rating
        fields = ('star',)
