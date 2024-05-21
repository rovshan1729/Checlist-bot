# Generated by Django 5.0.6 on 2024-05-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0020_usernotification"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="fail_count",
            field=models.PositiveIntegerField(
                blank=True, default=0, null=True, verbose_name="Fail Count"
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="sent_count",
            field=models.PositiveIntegerField(
                blank=True, default=0, null=True, verbose_name="Sent Count"
            ),
        ),
    ]
