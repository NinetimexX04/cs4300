# bookings/views.py
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


# ---- DRF API ViewSets ----
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by("id")
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by("seat_number")
    serializer_class = SeatSerializer

    # POST /api/seats/{id}/book/ with JSON: {"movie": <movie_id>}
    @action(detail=True, methods=["post"])
    def book(self, request, pk=None):
        seat = self.get_object()
        if seat.is_booked:
            return Response({"detail": "Seat already booked."}, status=400)

        movie_id = request.data.get("movie")
        try:
            movie = Movie.objects.get(pk=movie_id)  # uses your Movie model
        except (Movie.DoesNotExist, TypeError, ValueError):
            return Response({"detail": "Valid 'movie' id required."}, status=400)

        # Allow guest booking: user is None if anonymous
        user = request.user if getattr(request, "user", None) and request.user.is_authenticated else None

        booking = Booking.objects.create(movie=movie, seat=seat, user=user)
        seat.is_booked = True
        seat.save(update_fields=["is_booked"])
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("movie", "seat", "user").order_by("-booked_at")
    serializer_class = BookingSerializer

    # Show ALL bookings (no per-user filter)
    # If you prefer to keep "history" per session later, we can add that—but not needed for this assignment.
    def get_queryset(self):
        return self.queryset


# ---- Template (HTML) Views ----
def movie_list(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})


def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    seats = Seat.objects.all().order_by("seat_number")

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, pk=seat_id)
        if seat.is_booked:
            return render(
                request,
                "bookings/seat_booking.html",
                {"movie": movie, "seats": seats, "error": "Seat is already booked."},
            )
        user = request.user if getattr(request, "user", None) and request.user.is_authenticated else None
        Booking.objects.create(movie=movie, seat=seat, user=user)
        seat.is_booked = True
        seat.save(update_fields=["is_booked"])
        return redirect("booking_history")

    return render(request, "bookings/seat_booking.html", {"movie": movie, "seats": seats})


def booking_history(request):
    # Show ALL bookings (since there is no login)
    bookings = Booking.objects.select_related("movie", "seat").order_by("-booked_at")
    return render(request, "bookings/booking_history.html", {"bookings": bookings})
