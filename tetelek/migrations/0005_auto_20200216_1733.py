# Generated by Django 3.0.3 on 2020-02-16 16:33

from django.db import migrations, models
import tetelek.models


class Migration(migrations.Migration):

    dependencies = [
        ('tetelek', '0004_auto_20200204_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tetelek',
            name='photo',
            field=models.ImageField(default='images/default.jpg', upload_to=tetelek.models.path_and_rename),
        ),
    ]
