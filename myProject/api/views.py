from django.shortcuts import render

# Create your views here.
# yourapp/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Car, WheelForm, WheelField
from .serializers import CarSerializer, WheelFormSerializer, WheelFieldSerializer
from rest_framework.permissions import AllowAny

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Car registered successfully!",
            "data": response.data,
            "status": "success",

        })

class WheelFormViewSet(viewsets.ModelViewSet):
    queryset = WheelForm.objects.all()
    serializer_class = WheelFormSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Wheel form registered successfully!",
            "status": "success",
            "data": response.data,

        })

class WheelFieldViewSet(viewsets.ModelViewSet):
    queryset = WheelField.objects.all()
    serializer_class = WheelFieldSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Wheel field registered successfully!",
            "status": "success",
            "data": response.data,
        })