# Generated by Django 4.1.1 on 2022-10-25 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 25, 12, 38, 56, 460723)),
        ),
    ]
