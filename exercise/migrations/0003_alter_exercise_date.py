# Generated by Django 4.1.1 on 2022-11-01 00:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_exercise_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 8, 31, 35, 512619)),
        ),
    ]
