# Generated by Django 5.0.6 on 2024-07-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_main", "0010_vendor_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseorder",
            name="IaSubmissionDate",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="InspectionDate",
            field=models.DateField(null=True),
        ),
    ]
