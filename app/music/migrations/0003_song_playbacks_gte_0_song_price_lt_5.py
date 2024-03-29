# Generated by Django 5.0.2 on 2024-02-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0002_alter_song_deal_of_the_day"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="song",
            constraint=models.CheckConstraint(
                check=models.Q(("playbacks__gte", 0)), name="playbacks_gte_0"
            ),
        ),
        migrations.AddConstraint(
            model_name="song",
            constraint=models.CheckConstraint(
                check=models.Q(("price__lt", 5)), name="price_lt_5"
            ),
        ),
    ]
