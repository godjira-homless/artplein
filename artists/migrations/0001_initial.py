# Generated by Django 3.0.1 on 2019-12-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('bio', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Művészek',
            },
        ),
    ]
