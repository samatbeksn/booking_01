from django.urls import path
from .views import *


urlpatterns = [

    path('users/', UserProfileViewSet.as_view({'get': 'list',
                                               'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                        'put': 'update',
                                                        'delete': 'destroy'}), name='user_detail'),
    path('', HotelViewSet.as_view({'get': 'list',
                                   'post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelViewSet.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'delete': 'destroy'}), name='hotel_detail'),
    path('hotel_photos/', HotelPhotosViewSet.as_view({'get': 'list',
                                                     'post': 'create'}), name='hotel_photos_list'),
    path('hotel_photos/<int:pk>/', HotelPhotosViewSet.as_view({'get': 'retrieve',
                                                               'put': 'update',
                                                               'delete': 'destroy'}), name='hotel_photos_detail'),

    path('room/', RoomViewSet.as_view({'get': 'list',
                                       'post': 'create'}), name='room_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve',
                                                'put': 'update',
                                                'delete': 'destroy'}), name='room_detail'),

    path('room_photos/', RoomPhotosViewSet.as_view({'get': 'list',
                                                    'post': 'create'}), name='room_photos_list'),
    path('room_photos/<int:pk>/', RoomPhotosViewSet.as_view({'get': 'retrieve',
                                                             'put': 'update',
                                                             'delete': 'destroy'}), name='room_photos_detail'),

    path('booking/', BookingViewSet.as_view({'get': 'list',
                                            'post': 'create'}), name='booking_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve',
                                                     'put': 'update',
                                                      'delete': 'destroy'}), name='booking_detail'),
]
