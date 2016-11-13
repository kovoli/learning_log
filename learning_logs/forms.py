from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic           # model = присваивается модель Topics
        fields = ['text']       # fields = импортирует только поле text
        labels = {'text': ''}   # не генериро- вать подпись для текстового поля

