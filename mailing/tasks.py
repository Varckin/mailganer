from .celery import app as celery_app
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Mailing, Subscriber, Tracking
import uuid

@celery_app.task
def send_mailing(mailing_id):
    mailing = Mailing.objects.get(id=mailing_id)
    for subscriber in mailing.subscribers.all():
        context = {
            'first_name': subscriber.first_name,
            'last_name': subscriber.last_name,
            'birthday': subscriber.birthday,
        }
        html_content = render_to_string('mailing/email_template.html', context)
        tracking_uuid = uuid.uuid4()
        Tracking.objects.create(
            mailing=mailing,
            subscriber=subscriber,
            uuid=tracking_uuid
        )
        tracking_url = f'http://yourdomain.com/tracking/{tracking_uuid}.png'
        html_content += f'<img src="{tracking_url}" width="1" height="1" />'
        msg = EmailMultiAlternatives(
            mailing.subject,
            'Email content',
            'noreply@yourdomain.com',
            [subscriber.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    mailing.status = 'sent'
    mailing.save()