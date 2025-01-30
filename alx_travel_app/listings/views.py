from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from .models import Booking
from .serializers import BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
