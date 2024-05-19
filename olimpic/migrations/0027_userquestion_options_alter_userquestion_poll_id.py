# Generated by Django 5.0.6 on 2024-05-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("olimpic", "0026_userquestion_poll_id_userquestion_user_olimpic"),
    ]

    operations = [
        migrations.AddField(
            model_name="userquestion",
            name="options",
            field=models.ManyToManyField(
                related_name="user_questions", to="olimpic.option"
            ),
        ),
        migrations.AlterField(
            model_name="userquestion",
            name="poll_id",
            field=models.CharField(blank=True, db_index=True, null=True),
        ),
    ]
