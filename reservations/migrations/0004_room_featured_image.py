# Generated by Django 5.1.2 on 2024-11-08 19:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_room_view_alter_room_bed_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]