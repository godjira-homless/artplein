from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.urls import reverse
from artists.models import Artist
from technics.models import Technic


class AjaxManager(models.Manager):

    def last_code(self):
        next_code = Ajax.objects.filter().order_by('-code').first()
        if next_code:
            next_code = next_code
        else:
            next_code = 1
        # return super().get_queryset().filter(Q(name__icontains='bútor') | Q(name__icontains='ezüst'))
        return next_code


class Ajax(models.Model):
    code = models.IntegerField(blank=False, default=None)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=50, blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=False, default=1, on_delete=models.SET_DEFAULT)
    tech = models.ForeignKey(Technic, null=True, blank=False, default=1, on_delete=models.SET_DEFAULT)
    slug = models.SlugField(null=False, unique=True)
    objects = AjaxManager()

    class Meta:
        managed = True

    def __str__(self):
        return str(self.code)

    def get_absolute_url(self):
        return reverse('ajax_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
