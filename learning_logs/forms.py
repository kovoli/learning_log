from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic           # model = присваивается модель Topics
        fields = ['text']       # fields = импортирует только поле text
        labels = {'text': 'Категория'}   # Сгенерирует подпись для текстового поля

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Содержание'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

"""Виджет (widget) представляет собой элемент формы HTML:
однострочное или многострочное текстовое поле, раскрывающийся список и т. д.
Включая атрибут widgets, вы можете переопределить виджеты, выбранные Django по умолчанию.
Приказывая Django использовать элемент forms. Textarea, мы настраиваем виджет ввода для поля 'text',
чтобы ширина текстовой области составляла 80 столбцов вместо значения по умолчанию 40"""


