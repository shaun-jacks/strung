from django.contrib import admin

from .models import Hangout, Comment

admin.site.register(Hangout)
admin.site.register(Comment)