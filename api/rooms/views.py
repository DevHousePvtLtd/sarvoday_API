from rest_framework import viewsets
from .serializers import RoomSerializer
from .models import Rooms


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all().order_by('room_no')
    serializer_class = RoomSerializer
