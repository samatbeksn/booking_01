from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'text', 'video', 'type', 'price']


class HotelPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
