# Generated by Django 2.1 on 2020-02-02 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tetelek', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tetelek',
            name='artist',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='artists.Artist'),
        ),
    ]
