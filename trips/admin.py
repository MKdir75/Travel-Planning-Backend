from django.contrib import admin
from .models import Trip, Hotel, Transport

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('destination', 'start_date', 'end_date', 'hotel', 'transport')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price')

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('type', 'company', 'price')
