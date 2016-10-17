from django.contrib import admin
from .models import Place, Post
from import_export.admin import ExportMixin
from import_export import resources

class PlaceAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ('name', 'poiid',)


class PostResource(resources.ModelResource):

    class Meta:
        model = Post
        exclude = ('weibo_thumb_img', )

class PostAdmin(ExportMixin, admin.ModelAdmin):
    search_fields = ['id', 'place', 'category']
    list_filter = ['place', 'category']
    list_display = ('id', 'place', 'created', 'category')

admin.site.register(Place, PlaceAdmin)
admin.site.register(Post, PostAdmin)