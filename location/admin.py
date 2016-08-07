from django.contrib import admin
from .models import Place, Post
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ('name', 'poiid',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ['id', 'place', 'category']
    list_filter = ['place', 'category']
    list_display = ('id', 'place', 'created', 'category')

admin.site.register(Place, PlaceAdmin)
admin.site.register(Post, PostAdmin)