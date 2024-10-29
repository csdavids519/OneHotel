from django.db import models


# Create your models here.
class Bookings(models.Model):
    booking_code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.booking_code
    

class Rooms(models.Model):
    ROOM_TYPE = (
        ('1','Basic'),
        ('2','Premium'),
        ('3','Executive'),
    )

    BED_TYPE = (
        ('1','Single Bed'),
        ('2','Double Bed'),
        ('3','Queen Bed'),
    )

    room_number = models.IntegerField(unique=True)
    room_type = models.CharField( null=True, choices= ROOM_TYPE)
    floor = models.IntegerField()
    bed_type = models.CharField( null=True, choices= BED_TYPE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_code = models.ForeignKey(
        Bookings, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_number)


class Customer(models.Model):
    customer_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    booking_code = models.ForeignKey(
        Bookings, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name
    
    def __str__(self):
        return self.customer_id


