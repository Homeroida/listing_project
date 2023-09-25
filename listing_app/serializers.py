from rest_framework import serializers
from .models import Photo, Location, Listing, Status


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
# Create serializers for Location, Listing, and Status models similarly.
