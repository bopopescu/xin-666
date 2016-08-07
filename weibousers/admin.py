from django.contrib import admin
from .models import WeiboUser
# Register your models here.

class WeiboUserAdmin(admin.ModelAdmin):
    list_filter = ['gender',]
    list_display = ('weibo_name', 'weibo_id', 'gender', 'province', 'city', 'location')

admin.site.register(WeiboUser, WeiboUserAdmin)