from rest_framework import generics
from LightController.models import Light, Controller
from LightController.serializers import LightSerializer, ControllerSerializer

__author__ = 'james'




class LightDetail(generics.RetrieveUpdateAPIView):
    model = Light
    serializer_class = LightSerializer
    lookup_field = 'light_id'

class ControllerDetail(generics.RetrieveAPIView):
    model = Controller
    serializer_class = ControllerSerializer
    lookup_field = 'pk'