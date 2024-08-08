from django.db import models
from django.contrib.auth.models import User


class NewsletterSubscriber(models.Model):
    subscriber = models.EmailField(unique=True, max_length=60)

    def __str__(self):
        return self.subscriber

class Newsletter(models.Model):
    subject = models.CharField(max_length=120)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Newsletter {self.subject} sent on {self.created_on}"

    def get_subscribers(self):
        return NewsletterSubscriber.objects.all()
