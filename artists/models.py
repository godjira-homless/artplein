from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=120, blank=False)
    bio = models.CharField(max_length=120, blank=True)


    class Meta:
        verbose_name_plural = "Művészek"

    def __str__(self):
        return str(self.name)
