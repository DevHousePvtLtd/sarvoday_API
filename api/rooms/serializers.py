from django.db.models import fields
from rest_framework import serializers
from .models import Rooms


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rooms
        fields = ('room_no', 'room_desc', 'room_cat',
                  'price', 'capacity', 'no_of_beds')
