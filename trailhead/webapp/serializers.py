#purpose: convert trip model instances to JSON and validate incoming JSON data
#author: Sammy Rago
#date: 10/26/24

from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'trip_name', 'trip_date', 'trip_description', 'trip_leader', 'trip_capacity', 'subclub']