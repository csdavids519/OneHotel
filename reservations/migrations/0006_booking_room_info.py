# Generated by Django 5.1.2 on 2024-11-14 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0005_booking_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="room_info",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="bookings",
                to="reservations.room",
            ),
        ),
    ]
