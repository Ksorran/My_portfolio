from django import forms

from portfolio.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('contacts', 'feedback')
        widgets = {
            'contacts': forms.TextInput(attrs={'class': 'feedback-input'}),
            'feedback': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'feedback-text-area'}),
        }

