# Generated by Django 4.2.7 on 2023-12-29 23:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("billing_app", "0003_rename_datetime_bill_datetime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="appointmentId",
            field=models.CharField(),
        ),
    ]
