from django.shortcuts import render, redirect
from django.http import Http404
from datetime import datetime
from shortener.urls.models import Urls

domain = 'http://127.0.0.1:8000'


# Create your views here.
def shorten(request):
    target = request.POST['target']
    token = Urls.generate_unique_token()
    short_url = '%/r/%' % (domain, token)
    now = datetime.now()
    url = Urls(token=token, target=target, short_url=short_url, created_at=now)
    url.save()


def r(request, token):
    url = Urls.objects.get(token=token)

    if url:
        redirect(url['short_url'])

    raise Http404
