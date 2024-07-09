# Generated by Django 5.0.6 on 2024-07-09 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0020_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="VendorNo",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_main.vendor",
            ),
        ),
    ]
