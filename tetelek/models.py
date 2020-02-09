from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from artists.models import Artist
from django.conf import settings


class TetelManager(models.Manager):

    def last_code(self):
        next_code = Tetelek.objects.filter().order_by('-code').first()
        if next_code:
            next_code = next_code
        else:
            next_code = 1
        # return super().get_queryset().filter(Q(name__icontains='bútor') | Q(name__icontains='ezüst'))
        return next_code


class Tetelek(models.Model):
    code = models.IntegerField(blank=False, default=None, unique=True)
    title = models.CharField(max_length=120, blank=False)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, related_name='created', on_delete=models.SET('1'))
    modified_by = models.ForeignKey(User, null=True, related_name='modified', on_delete=models.SET('1'))
    slug = models.SlugField(null=False, unique=True)
    objects = TetelManager()

    def __str__(self):
        return str(str(self.code))

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
