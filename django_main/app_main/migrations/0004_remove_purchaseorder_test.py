# Generated by Django 5.0.6 on 2024-06-28 05:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0003_purchaseorder_test"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="purchaseorder",
            name="test",
        ),
    ]
