import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Study(models.Model):
    ACCESS_LEVEL = (
        ('public', 'Open&Free = is or could be made publicly available to all without restrictions'),
        ('restricted-public', 'Available, with some rules = available under certain use restrictions'),
        ('non-public', 'Private  = not available to members of the public'),
        )
    LANGUAGE = (
        ('English', 'English'),
        ('French', 'Français'),
        ('Italian', 'Italiano'),
        ('Spanish', 'Español'),
        )
    title = models.CharField(max_length=254)
    description = models.TextField()
    # tags = need to figure out if using taggit, many-to-many, or arrayfield
    pub_date = models.DateTimeField('date published')
    last_update = models.DateField(auto_now=True)
    publisher = models.CharField(max_length=254)
    contactPoint = models.CharField(max_length=254)
    mbox = models.EmailField(max_length=254)
    identifier = models.CharField(max_length=254)
    accessLevel = models.CharField(max_length=10, choices=ACCESS_LEVEL, default="public")
    landingPage = models.URLField(max_length=200)
    language = models.CharField(max_length=30, choices=LANGUAGE, default="English")
    issued = models.DateField(auto_now=False, auto_now_add=False)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/')
    times_seen = models.IntegerField(default=0)
    def __str__(self):
        return 'Study #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'studies'

    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

   # def total_times_seen(self):
   #     return times_seen =+ 1