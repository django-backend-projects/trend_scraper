# Generated by Django 4.1.5 on 2023-08-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_excellasaninfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExcellDeclInfo",
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
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="created date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="updated date"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Ad")),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="excell_files/",
                        verbose_name="Excell fayl",
                    ),
                ),
            ],
            options={
                "verbose_name": "Excell fayl",
                "verbose_name_plural": "Excell fayllar",
            },
        ),
    ]
