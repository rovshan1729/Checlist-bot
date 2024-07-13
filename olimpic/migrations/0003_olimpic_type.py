# Generated by Django 5.0.6 on 2024-07-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("olimpic", "0002_alter_question_duration"),
    ]

    operations = [
        migrations.AddField(
            model_name="olimpic",
            name="type",
            field=models.CharField(
                choices=[("Olimpiada", "Olimpiada"), ("Simulyator", "Simulyator")],
                db_index=True,
                default="Simulyator",
                max_length=25,
                verbose_name="Type",
            ),
        ),
    ]
