# Generated by Django 4.1.1 on 2022-12-07 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
