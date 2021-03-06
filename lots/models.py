from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from artists.models import Artist


class Lots(models.Model):
    code = models.IntegerField(blank=False, default=None, unique=True)
    title = models.CharField(max_length=120, blank=False, null=False)
    artist = models.ForeignKey(Artist, null=True, blank=False, default=0, on_delete=models.SET_DEFAULT)
    size = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    # user = models.OneToOneField(User, default=1, on_delete=models.SET_DEFAULT, blank=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, blank=True, related_name='%(class)s_created', on_delete=models.SET('1'))
    modified_by = models.ForeignKey(User, null=True, related_name='%(class)s_modified', on_delete=models.SET('1'))

    def __str__(self):
        return str(self.code)

    def get_absolute_url(self):
        return reverse('detail_lot', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # self.slug = slugify(self.title)
            self.slug = self.get_unique_slug(self.id, self.title, Lots.objects)
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
