# Generated by Django 5.0.6 on 2024-07-09 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0023_remove_users_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="username",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_main.users",
            ),
        ),
    ]