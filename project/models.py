from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    champion = models.ForeignKey(User, null=True, blank=False, default=1, on_delete=models.SET_DEFAULT)
