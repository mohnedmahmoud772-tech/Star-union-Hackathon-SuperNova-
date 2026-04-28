from django.contrib import admin
from .models import Provider, Receiver, Volunteer

admin.site.register((Provider, Receiver, Volunteer))