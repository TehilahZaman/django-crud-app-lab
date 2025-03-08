from django.contrib import admin

# Register your models here.
from .models import Postit, Reminder
admin.site.register(Postit)
admin.site.register(Reminder)
