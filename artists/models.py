from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=120)
    bio = models.CharField(max_length=120)


    class Meta:
        verbose_name_plural = "Művészek"

    def __str__(self):
        return self.name
