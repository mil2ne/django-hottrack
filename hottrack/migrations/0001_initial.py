# Generated by Django 4.2.13 on 2024-05-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("melon_uid", models.CharField(max_length=20, unique=True)),
                ("rank", models.PositiveSmallIntegerField()),
                ("album_name", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("artist_name", models.CharField(max_length=100)),
                ("cover_url", models.URLField()),
                ("lyrics", models.TextField()),
                ("genre", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                ("like_count", models.PositiveIntegerField()),
            ],
        ),
    ]
