from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Technic(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('technic_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        #if not self.slug:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
