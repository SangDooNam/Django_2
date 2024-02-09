# Generated by Django 5.0.2 on 2024-02-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0003_song_playbacks_gte_0_song_price_lt_5"),
    ]

    operations = [
        migrations.CreateModel(
            name="Audio",
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
                ("audio", models.FileField(upload_to="audio/")),
                ("title", models.CharField(max_length=250)),
                ("author", models.CharField(blank=True, db_index=True, max_length=50)),
                ("author_website", models.URLField(blank=True)),
                ("album", models.CharField(blank=True, max_length=250)),
                ("duration", models.DurationField()),
                (
                    "song_style",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("rock", "Rock"),
                            ("pop", "Pop"),
                            ("indie", "Indie"),
                            ("funky", "Funky"),
                            ("classic", "Classic"),
                            ("reggaeton", "Reggaeton"),
                            ("funky", "Funky"),
                        ],
                        max_length=20,
                    ),
                ),
                ("playbacks", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("deal_of_the_day", models.BooleanField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("song", "Song"),
                            ("podcast", "Podcast"),
                            ("effect", "Effect"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Song",
        ),
        migrations.AddConstraint(
            model_name="audio",
            constraint=models.UniqueConstraint(
                fields=("title", "author", "duration"),
                name="Unique_title_author_duration",
            ),
        ),
        migrations.AddConstraint(
            model_name="audio",
            constraint=models.CheckConstraint(
                check=models.Q(("playbacks__gte", 0)), name="playbacks_gte_0"
            ),
        ),
        migrations.AddConstraint(
            model_name="audio",
            constraint=models.CheckConstraint(
                check=models.Q(("price__lt", 5)), name="price_lt_5"
            ),
        ),
    ]