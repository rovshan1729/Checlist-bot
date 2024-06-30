# Generated by Django 5.0.6 on 2024-06-30 14:58

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bot", "0001_initial"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Olimpic",
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
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "title_uz",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "title_ru",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=255, null=True, verbose_name="Title"),
                ),
                (
                    "description",
                    ckeditor.fields.RichTextField(verbose_name="Description"),
                ),
                (
                    "description_uz",
                    ckeditor.fields.RichTextField(
                        null=True, verbose_name="Description"
                    ),
                ),
                (
                    "description_ru",
                    ckeditor.fields.RichTextField(
                        null=True, verbose_name="Description"
                    ),
                ),
                (
                    "description_en",
                    ckeditor.fields.RichTextField(
                        null=True, verbose_name="Description"
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="olimpics"),
                ),
                ("file_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "start_time",
                    models.DateTimeField(db_index=True, verbose_name="Start Time"),
                ),
                (
                    "end_time",
                    models.DateTimeField(db_index=True, verbose_name="End Time"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="Is Active"
                    ),
                ),
                (
                    "result_publish",
                    models.DateTimeField(
                        db_index=True, null=True, verbose_name="Result Publish"
                    ),
                ),
                (
                    "certificate_generate",
                    models.DateTimeField(
                        db_index=True, null=True, verbose_name="Certificate Generate"
                    ),
                ),
                (
                    "is_all_users",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="Is All Users"
                    ),
                ),
                (
                    "class_room",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("5-sinf", "5-sinf"),
                            ("6-sinf", "6-sinf"),
                            ("7-sinf", "7-sinf"),
                            ("8-sinf", "8-sinf"),
                            ("9-sinf", "9-sinf"),
                            ("10-sinf", "10-sinf"),
                            ("11-sinf", "11-sinf"),
                        ],
                        db_index=True,
                        max_length=255,
                        null=True,
                        verbose_name="Class Room",
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="olimpic_districts",
                        to="common.district",
                        verbose_name="District",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="olimpic_regions",
                        to="common.region",
                        verbose_name="Region",
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="olimpic_schools",
                        to="common.school",
                        verbose_name="School",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OlimpicCertifeicate",
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
                (
                    "certificate",
                    models.ImageField(blank=True, null=True, upload_to="certificates"),
                ),
                (
                    "olimpic",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="certificate",
                        to="olimpic.olimpic",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                ("text", ckeditor.fields.RichTextField(verbose_name="Text")),
                (
                    "text_uz",
                    ckeditor.fields.RichTextField(null=True, verbose_name="Text"),
                ),
                (
                    "text_ru",
                    ckeditor.fields.RichTextField(null=True, verbose_name="Text"),
                ),
                (
                    "text_en",
                    ckeditor.fields.RichTextField(null=True, verbose_name="Text"),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Duration (seconds)"
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="questions"),
                ),
                (
                    "file_content",
                    models.FileField(blank=True, null=True, upload_to="questions"),
                ),
                (
                    "olimpic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="olimpic.olimpic",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Option",
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
                ("title", models.CharField(max_length=255)),
                ("title_uz", models.CharField(max_length=255, null=True)),
                ("title_ru", models.CharField(max_length=255, null=True)),
                ("title_en", models.CharField(max_length=255, null=True)),
                ("is_correct", models.BooleanField(db_index=True, default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="options",
                        to="olimpic.question",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserOlimpic",
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
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                ("olimpic_duration", models.DurationField(blank=True, null=True)),
                ("correct_answers", models.PositiveIntegerField(blank=True, null=True)),
                ("wrong_answers", models.PositiveIntegerField(blank=True, null=True)),
                ("not_answered", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "certificate",
                    models.FileField(blank=True, null=True, upload_to="certificates"),
                ),
                (
                    "olimpic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_olimpics",
                        to="olimpic.olimpic",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_olimpics",
                        to="bot.telegramprofile",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserQuestion",
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
                ("is_sent", models.BooleanField(db_index=True, default=False)),
                ("is_answered", models.BooleanField(db_index=True, default=False)),
                ("is_correct", models.BooleanField(db_index=True, default=False)),
                ("message_id", models.PositiveBigIntegerField(default=0)),
                ("content_message_id", models.PositiveBigIntegerField(default=0)),
                ("poll_id", models.CharField(blank=True, db_index=True, null=True)),
                ("task_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "next_task_id",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "olimpic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_questions",
                        to="olimpic.olimpic",
                    ),
                ),
                (
                    "options",
                    models.ManyToManyField(
                        related_name="user_questions", to="olimpic.option"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_questions",
                        to="olimpic.question",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_questions",
                        to="bot.telegramprofile",
                    ),
                ),
                (
                    "user_olimpic",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_questions",
                        to="olimpic.userolimpic",
                    ),
                ),
                (
                    "user_option",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_options",
                        to="olimpic.option",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserQuestionOption",
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
                ("order", models.PositiveIntegerField(db_index=True)),
                (
                    "option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_question_options",
                        to="olimpic.option",
                    ),
                ),
                (
                    "user_question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_question_options",
                        to="olimpic.userquestion",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
