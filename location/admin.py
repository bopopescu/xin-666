from django.contrib import admin
from .models import Place, Post
from import_export.admin import ExportMixin
from reversion.admin import VersionAdmin

class PlaceAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ('name', 'poiid',)

class PostAdmin(VersionAdmin):
    search_fields = ['id', 'place__name', 'category__name']
    list_filter = ['place', 'category']
    list_display = ('id', 'place', 'created', 'category')

admin.site.register(Place, PlaceAdmin)
admin.site.register(Post, PostAdmin)