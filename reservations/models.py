from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Room(models.Model):
    ROOM_TYPE = (
        ('Basic','Basic'),
        ('Premium','Premium'),
        ('Executive','Executive'),
    )

    BED_TYPE = (
        ('Single','Single'),
        ('Double','Double'),
        ('Queen','Queen'),
    )

    VIEW = (
        ('Ocean','Ocean'),
        ('City','City'),
    )

    room_number = models.IntegerField(unique=True)
    room_type = models.CharField(null=True, choices=ROOM_TYPE)
    floor = models.IntegerField(null=True)
    bed_type = models.CharField( null=True, choices=BED_TYPE)
    view = models.CharField(null=True, choices=VIEW)
    room_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return str(self.room_number)


class Customer(models.Model):
    customer_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.customer_number} - {self.last_name}"


class Booking(models.Model):
    STATUS = (
        ('APPROVED','APPROVED'),
        ('In Review','In Reivew'),
    )

    booking_code = models.CharField(max_length=5, blank=True, null=True, unique=True)
    reserved_start_date = models.DateField(null=True, blank=True)
    reserved_end_date = models.DateField(null=True, blank=True)
    room_number = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(blank=True, null=True)
    status = models.CharField( default='In Review', choices=STATUS)
    room_info = models.ForeignKey(Room, on_delete=models.DO_NOTHING, related_name='bookings', null=True, blank=True)


    def __str__(self):
        return str(self.booking_code)
    