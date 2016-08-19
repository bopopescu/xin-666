from django.db import models
from django.utils import timezone
from weibousers.models import WeiboUser


class Place(models.Model):
    name = models.CharField(db_index=True, max_length=120)
    poiid = models.CharField(db_index=True, max_length=120)
    province = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    place =  models.ForeignKey(Place)
    user = models.ForeignKey(WeiboUser)
    weibo_id = models.BigIntegerField(null=True, blank=True, unique=True)
    created = models.DateField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    weibo_img = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey('categories.Category', blank=True, null=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s' % (self.weibo_id,)
