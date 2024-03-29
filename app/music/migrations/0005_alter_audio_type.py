# Generated by Django 5.0.2 on 2024-02-09 21:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0004_audio_delete_song_audio_unique_title_author_duration_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="type",
            field=models.CharField(
                choices=[
                    ("song", "Song"),
                    ("podcast", "Podcast"),
                    ("effect", "Effect"),
                ],
                max_length=10,
            ),
        ),
    ]
