# Generated by Django 5.0.6 on 2024-07-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0013_remove_vendor_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="Password",
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
    ]