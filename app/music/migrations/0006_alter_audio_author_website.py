# Generated by Django 5.0.2 on 2024-02-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0005_alter_audio_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audio",
            name="author_website",
            field=models.URLField(blank=True, null=True),
        ),
    ]
