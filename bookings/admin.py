# bookings/admin.py

from django.contrib import admin
from .models import Movie, Booking

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','trailer_url','booking_summary')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'poster', 'trailer_url')
        }),
    )

    inlines = [
        BookingInline,
    ]

    def booking_summary(self, obj):
        bookings = Booking.objects.filter(movie=obj)
        total_bookings = bookings.count()
        return f'Total bookings: {total_bookings}'

    booking_summary.short_description = 'Booking Summary'
