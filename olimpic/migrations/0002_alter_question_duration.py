# Generated by Django 5.0.6 on 2024-07-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("olimpic", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="duration",
            field=models.PositiveIntegerField(
                default=60, verbose_name="Duration (seconds)"
            ),
        ),
    ]
