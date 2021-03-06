# Generated by Django 3.0.2 on 2020-01-27 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20200105_1124'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lots',
            name='user',
        ),
        migrations.AddField(
            model_name='lots',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('1'), related_name='lots_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lots',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=models.SET('1'), related_name='lots_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lots',
            name='artist',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='artists.Artist'),
        ),
    ]
