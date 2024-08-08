from .forms import SubscriberForm

def subscriber_form_processor(request):
    subscriber_form = SubscriberForm()
    return {
        'subscriber_form': subscriber_form
    }
