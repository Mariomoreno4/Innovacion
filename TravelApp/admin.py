from django.contrib import admin

from .models import  Place, Favorite, Comment, Like


admin.site.register(Place)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Like)