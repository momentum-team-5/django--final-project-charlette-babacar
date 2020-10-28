from .models import Question, Answer
from django.core.exceptions import ValidationError
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question',
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            "answer",
        ]

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(required=True, max_length=255)
    body = forms.CharField(label="Message", widget=forms.Textarea(attrs={'required': True}))


class SearchForm(forms.Form):
    question = forms.CharField(max_length=255)