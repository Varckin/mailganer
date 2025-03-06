from django.db import models
from django.utils import timezone
import uuid


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)


class Mailing(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('sent', 'Sent'),
    )
    subject = models.CharField(max_length=255)
    html_template = models.TextField()
    subscribers = models.ManyToManyField(Subscriber)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')


class Tracking(models.Model):
    mailing = models.ForeignKey(Mailing)
    subscriber = models.ForeignKey(Subscriber)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    