from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from artists.models import Artist


class Tetelek(models.Model):
    title = models.CharField(max_length=120, blank=False)
    artist = models.ForeignKey(Artist, null=True, blank=True, default=1, on_delete=models.SET_DEFAULT)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('detail_lot', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.title, Tetelek.objects)
        return super().save(*args, **kwargs)

    def get_unique_slug(self, id, title, obj):
        slug = slugify(title)
        unique_slug = slug
        counter = 1
        while obj.filter(slug=unique_slug).exists():
            if obj.filter(slug=unique_slug).values('id')[0]['id'] == id:
                break
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
