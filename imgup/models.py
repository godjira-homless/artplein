from django.db import models


class Imguploads(models.Model):
    title = models.CharField(max_length=120, blank=False)
    # photo = models.ImageField(upload_to='images/', default='images/default.jpg')
    file = models.FileField(max_length=100, upload_to="documents/", default='images/default.jpg')

    def __str__(self):
        return str(str(self.title))