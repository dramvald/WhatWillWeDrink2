# Generated by Django 3.2.3 on 2021-05-26 18:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drink", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drink",
            name="ingredients",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=300, verbose_name="Ingredients"),
                size=None,
            ),
        ),
    ]
