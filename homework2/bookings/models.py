# bookings/models.py
from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(default=0, help_text="minutes")
    def __str__(self):
        return self.title

class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.seat_number} ({'booked' if self.is_booked else 'free'})"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    seat = models.OneToOneField(Seat, on_delete=models.PROTECT, related_name="booking")
    # ↓↓↓ make user optional
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    booked_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user or 'Guest'} -> {self.movie} / {self.seat}"
