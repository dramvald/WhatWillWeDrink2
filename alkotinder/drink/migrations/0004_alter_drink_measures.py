# Generated by Django 3.2.3 on 2021-05-30 21:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drink", "0003_alter_drink_ingredients"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drink",
            name="measures",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=300, verbose_name="Measures"),
                blank=True,
                size=None,
            ),
        ),
    ]
