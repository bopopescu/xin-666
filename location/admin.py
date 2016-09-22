from django.contrib import admin
from .models import Place, Post
from import_export.admin import ImportExportModelAdmin

class PlaceAdmin(ImportExportModelAdmin):
    search_fields = ['name',]
    list_display = ('name', 'poiid',)


class PostAdmin(ImportExportModelAdmin):
    search_fields = ['id', 'place', 'category']
    list_filter = ['place', 'category']
    list_display = ('id', 'place', 'created', 'category')

admin.site.register(Place, PlaceAdmin)
admin.site.register(Post, PostAdmin)