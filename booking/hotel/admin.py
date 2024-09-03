from django.contrib import admin
from .models import *

from modeltranslation.admin import TranslationAdmin


@admin.register(Hotel)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(HotelPhotos)
admin.site.register(Room)
admin.site.register(RoomPhotos)
admin.site.register(Booking)

# Register your models here.
