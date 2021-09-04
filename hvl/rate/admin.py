from django.contrib import admin
from rate.models import Comment, Rating

admin.site.register(Rating)
admin.site.register(Comment)
