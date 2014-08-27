from rest_framework import serializers
from LightController.models import Light, Controller


class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Light
        fields = ('on', 'color', 'brightness')
        lookup_field = 'pk'

class ControllerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Controller
        fields = ('path', 'description', 'interface_type')
        lookup_field = 'pk'