from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.username


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    text = models.TextField()
    video = models.FileField(verbose_name='Видео', null=True, blank=True)
    type = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='STARS')
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.hotel_name


class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel_photos', on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='product_images/')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='room', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    persons = models.PositiveIntegerField(null=True, blank=True)

    def __int__(self):
        return self.quantity


class RoomPhotos(models.Model):
    room = models.ForeignKey(Room, related_name='room_photos', on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='product_images/')


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()



