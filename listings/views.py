from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing CRUD operations on Listing model.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing CRUD operations on Booking model.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
