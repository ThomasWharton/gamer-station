from django import forms
from .models import NewsletterSubscriber, Newsletter


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ('subscriber',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['subscriber'].widget.attrs['placeholder'] = "Enter your email"