from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import NewsletterSubscriber, Newsletter
from .forms import SubscriberForm


def subscribe(request):

    if request.method == 'POST':
        subscriber_form = SubscriberForm(data=request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Error in adding you to our newsletter subscriber list. \
                Please contact us for assistance.")

    return HttpResponseRedirect('/')
