from django import forms
from .models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['subject', 'html_template', 'scheduled_time', 'subscribers']
        widgets = {
            'subscribers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
