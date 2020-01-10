from django.db import models

from django.urls import reverse
from django.utils.text import slugify

from artists.models import Artist


class Lots(models.Model):
    code = models.IntegerField(blank=False, default=None, unique=True)
    title = models.CharField(max_length=120, blank=False, null=False)
    artist = models.ForeignKey(Artist, null=True, blank=False, default=1, on_delete=models.SET_DEFAULT)
    size = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return str(self.code)

    def get_absolute_url(self):
        return reverse('lots_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
