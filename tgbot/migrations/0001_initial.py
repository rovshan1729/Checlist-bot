# Generated by Django 4.2 on 2024-08-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TelegramProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("telegram_id", models.PositiveBigIntegerField()),
                ("username", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "full_name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Full Name"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Phone Number",
                    ),
                ),
            ],
            options={
                "verbose_name": "Telegram Profile",
                "verbose_name_plural": "Telegram Profiles",
                "db_table": "telegram_profiles",
            },
        ),
    ]
