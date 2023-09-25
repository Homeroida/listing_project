from rest_framework import viewsets
from .models import Photo, Location, Listing, Status
from .serializers import PhotoSerializer, LocationSerializer, ListingSerializer, StatusSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# Create ViewSets for Location, Listing, and Status models similarly.
