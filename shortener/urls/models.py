from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class Urls(models.Model):
    target = models.TextField()
    short_url = models.TextField()
    token = models.CharField(max_length=32, primary_key=True)
    created_at = models.DateField()

    def generate_unique_token(self):
        unique = False
        while not unique:
            token = uuid.uuid4().hex
            identical = list(Urls.objects.get(token=token))
            unique = not identical

        return token
