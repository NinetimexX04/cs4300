from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, book_seat, booking_history

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"seats", SeatViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("", movie_list, name="movie_list"),
    path("movies/<int:movie_id>/book/", book_seat, name="book_seat"),
    path("bookings/history/", booking_history, name="booking_history"),
    path("djadmin/", admin.site.urls),   # <-- This line makes /admin/ work
    path("api/", include(router.urls)),
]
