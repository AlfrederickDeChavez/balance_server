# Generated by Django 4.1.1 on 2022-11-01 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_food_date_consumed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
