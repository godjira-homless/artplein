from django.core.validators import RegexValidator
from django.db import models

alphanumeric = RegexValidator(r'^[0-9a-zA-ZáéíóőűöüúÁÉÍÓŐŰÚ]*$', 'Only alphanumeric characters are allowed.')

class Person(models.Model):
    first_name = models.CharField(max_length=30, validators=[alphanumeric])
    last_name = models.CharField(max_length=30)


    class Meta:
        verbose_name_plural = "Ügyfelek"

    def __str__(self):
        return self.first_name
