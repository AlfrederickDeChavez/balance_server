# Generated by Django 4.1.1 on 2022-11-01 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_alter_food_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]