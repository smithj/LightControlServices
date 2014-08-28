from django.shortcuts import render

# Create your views here.
import serial
from rest_framework import viewsets
from rest_framework.decorators import action
from LightController.models import Light, Controller
from rest_framework.response import Response
from LightController.serializers import LightSerializer


class LightViewSet(viewsets.ReadOnlyModelViewSet):
    model = Light


    def update(self, request, *args, **kwargs):
        data = request.DATA

        for key in data:
            print key
            print data[key]
            # kwargs[key] = data[key]
        print data

        return super(LightViewSet, self).update(request, *args, **kwargs)

    @action(methods=['PUT'])
    def set_color(self, request, pk=None):

        light = self.get_object()

        # get the serial controller to use, and the new value to set
        controller_path = light.controller.path
        new_color = int(request.DATA['color'], 0)

        # open serial port and send command
        ser = serial.Serial(controller_path, 9600, timeout=1)
        ser.write("SETCOL " + str(new_color))
        status = ser.readline()
        ser.close()

        # update the database for fun.
        serializer = LightSerializer(data=request.DATA)
        if serializer.is_valid():
            light.color = new_color
            light.save()

        print self

        return Response({'status': status})

    @action(methods=['PUT'])
    def set_delay(self, request, pk=None):

        light = self.get_object()

        # get the serial controller to use, and the new value to set
        controller_path = light.controller.path
        delay = request.DATA['delay']

        # open serial port and send command
        ser = serial.Serial(controller_path, 9600, timeout=1)
        ser.write("SETDLY " + str(delay))
        status = ser.readline()
        ser.close()

        # update the database for fun.
        serializer = LightSerializer(data=request.DATA)
        if serializer.is_valid():
            light.delay = delay
            light.save()

        print self

        return Response({'status': status})

    @action(methods=['PUT'])
    def set_brightness(self, request, pk=None):

        light = self.get_object()

        # get the serial controller to use, and the new value to set
        controller_path = light.controller.path
        brightness = request.DATA['brightness']

        # open serial port and send command
        ser = serial.Serial(controller_path, 9600, timeout=1)
        ser.write("SETBRT " + str(brightness))
        status = ser.readline()
        ser.close()

        # update the database for fun.
        serializer = LightSerializer(data=request.DATA)
        if serializer.is_valid():
            light.brightness = brightness
            light.save()

        print self

        return Response({'status': status})



class ControllerViewSet(viewsets.ReadOnlyModelViewSet):
    model = Controller



"""
class LightViewSet(viewsets.ModelViewSet):
    queryset = Light.objects.all()
    serializer_class = LightSerializer


class ControllerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'lights': reverse('light-list', request=request, format=format)
    })


"""

"""
@api_view(['GET', 'POST'])
def light_list(request):



    if request.method == 'GET':
        snippets = Light.objects.all()
        serializer = LightSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LightSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""