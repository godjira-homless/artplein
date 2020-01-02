from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.text import slugify


class TechnicManager(models.Manager):

    def nopaint_technics(self):
        return super().get_queryset().filter(Q(name__icontains='bútor') | Q(name__icontains='ezüst'))


class Technic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    objects = TechnicManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('technic_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        #if not self.slug:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

