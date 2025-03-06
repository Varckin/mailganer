from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from .models import Mailing, Tracking
from .forms import MailingForm
from datetime import timezone

@require_POST
def create_mailing(request):
    if request.is_ajax():
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.status = 'scheduled' if mailing.scheduled_time else 'draft'
            mailing.save()
            form.save_m2m()
            return JsonResponse({'success': True})
        return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def track_open(request, uuid):
    tracking = get_object_or_404(Tracking, uuid=uuid)
    if not tracking.opened_at:
        tracking.opened_at = timezone.now()
        tracking.save()
    response = HttpResponse(content_type='image/png')
    response.write(open('static/pixel.png', 'rb').read())
    return response
