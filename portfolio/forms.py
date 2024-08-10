from django import forms

from portfolio.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'telephone', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'feedback-input'}),
            'email': forms.TextInput(attrs={'class': 'feedback-input'}),
            'telephone': forms.TextInput(attrs={'class': 'feedback-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'feedback-text-area'}),
        }

