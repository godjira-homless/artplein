# Generated by Django 3.0.2 on 2020-01-18 17:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lots', '0002_auto_20200118_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lots',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL),
        ),
    ]