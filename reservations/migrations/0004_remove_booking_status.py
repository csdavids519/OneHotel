# Generated by Django 5.1.2 on 2024-11-14 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0003_remove_booking_status4_remove_booking_test"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="status",
        ),
    ]
