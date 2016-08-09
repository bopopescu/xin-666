from django.db import models
from django.utils import timezone
from datetime import datetime

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)

class WeiboUser(models.Model):
    weibo_id = models.BigIntegerField(null=True, blank=True, unique=True)
    weibo_name = models.CharField('weibo name', max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    province = models.PositiveSmallIntegerField(null=True, blank=True)
    city = models.PositiveSmallIntegerField(null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = 'weibo user'
        verbose_name_plural = 'weibo users'

    def __unicode__(self):
        return '%s' % (self.weibo_id,)
