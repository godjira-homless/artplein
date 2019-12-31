from django.db import models

# Create your models here.
class Appraisers(models.Model):
    name = models.CharField(max_length=120)


    class Meta:
        verbose_name_plural = "Becsüsők"
        ordering = ["name"]

    def __str__(self):
        return self.name