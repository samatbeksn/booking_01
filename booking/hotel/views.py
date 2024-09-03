from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import HotelFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class HotelPhotosViewSet(viewsets.ModelViewSet):
    queryset = HotelPhotos.objects.all()
    serializer_class = HotelPhotosSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomPhotosViewSet(viewsets.ModelViewSet):
    queryset = RoomPhotos.objects.all()
    serializer_class = RoomPhotosSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



