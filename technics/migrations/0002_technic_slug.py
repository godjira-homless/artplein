# Generated by Django 3.0.1 on 2020-01-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='technic',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
