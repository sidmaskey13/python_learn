from django import forms
from .models import Question,Choice


class PollQuestionForm(forms.ModelForm):
    question_text = forms.CharField(label='Question Title', widget=forms.TextInput())

    class Meta:
        model = Question
        fields = [
            'question_text',
        ]


class PollChoiceForm(forms.ModelForm):
    choice_text = forms.CharField(label='Choice 1', widget=forms.TextInput())
    question = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Choice
        fields = [
            'choice_text',
            'question',
        ]
