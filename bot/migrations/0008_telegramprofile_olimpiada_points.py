# Generated by Django 4.2.5 on 2024-07-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0007_alter_userproduct_verification_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="telegramprofile",
            name="olimpiada_points",
            field=models.PositiveIntegerField(
                blank=True, default=0, null=True, verbose_name="User Olympiad Points"
            ),
        ),
    ]
