from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsletterSubscriber, Newsletter
from .forms import SubscriberForm, NewsletterForm


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

def send_newsletter(newsletter):
    """Send the subscribers newsletter"""
    subscribers = newsletter.get_subscribers()
    subject = newsletter.subject
    body = newsletter.content

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [subscribers]
    )

def newsletter(request):
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Naughty boy!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid:
            newsletter = newsletter_form.save(commit=False)
            send_newsletter(newsletter=newsletter)
            newsletter.save()
            messages.success(request, 'Newsletter sent successfully!')
            return HttpResponseRedirect(reverse('home'))
        else:
            message.error(request, 'Error sending newsletter')
    else:
        newsletter_form = NewsletterForm()

    template = "newsletter/newsletter.html"

    context = {
        'newsletter_form': newsletter_form
    }

    return render(request, template, context)

