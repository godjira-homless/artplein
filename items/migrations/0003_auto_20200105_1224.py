# Generated by Django 3.0.2 on 2020-01-05 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_descriptiopn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='descriptiopn',
            new_name='description',
        ),
    ]
