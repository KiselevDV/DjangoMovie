"""
Формы
"""
from django import forms

# from ckeditor.widgets import CKEditorWidget
# Виджет для загрузки фалов - ckeditor_uploader
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Movie, Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')


class MovieAdminForm(forms.ModelForm):
    """
    Форма для модели Movie, с кастомным виджетом из 'ckeditor',
    для поля описания фильма (movie.description)
    """
    # Переопределяем стандартное поле
    description = forms.CharField(
        label='Описание',
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Movie
        fields = '__all__'
