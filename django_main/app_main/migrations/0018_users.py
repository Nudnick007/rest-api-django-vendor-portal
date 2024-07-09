# Generated by Django 5.0.6 on 2024-07-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0017_document_docname"),
    ]

    operations = [
        migrations.CreateModel(
            name="users",
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
                ("username", models.CharField(max_length=500)),
                (
                    "role",
                    models.CharField(
                        choices=[("admin", "Admin"), ("user", "User")],
                        default="user",
                        max_length=5,
                    ),
                ),
                ("password", models.CharField(max_length=500)),
            ],
        ),
    ]
