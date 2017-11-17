from django.shortcuts import render, redirect
from django.http import Http404

API_KEY = 'example123'

def authenticate(request, token):
    key = request.POST['api_key']

    if key == API_KEY:
        redirect(url['short_url'])

    raise Http404
