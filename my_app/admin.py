from django.contrib import admin

# Register your models here.
from .models import Postit, Reminder, Catagory
admin.site.register(Postit)
admin.site.register(Reminder)
admin.site.register(Catagory)