# Generated by Django 5.0.2 on 2024-02-09 22:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0008_alter_audio_type"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="audio",
            name="price_lt_5",
        ),
    ]
