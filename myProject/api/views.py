from django.shortcuts import render

# Create your views here.
# yourapp/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Car, WheelForm, WheelField, bogieDetailsForm, bogieChecksheetForm, bmbcChecksheetForm, bogieForm
from .serializers import CarSerializer, WheelFormSerializer, WheelFieldSerializer, bogieDetailsSerializer,bogieChecksheetSerializer, bmbcChecksheetSerializer,bogieSerializer
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

class bogieViewSet(viewsets.ModelViewSet):
    queryset = bogieForm.objects.all()
    serializer_class = bogieSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Bogie form registered successfully!",
            "status": "success",
            "data": response.data,
        })
class bogieDetailsViewSet(viewsets.ModelViewSet):
    queryset = bogieDetailsForm.objects.all()
    serializer_class = bogieDetailsSerializer 


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Bogie details registered successfully!",
            "status": "success",
            "data": response.data,
        })
class bogieChecksheetViewSet(viewsets.ModelViewSet):
    queryset = bogieChecksheetForm.objects.all()
    serializer_class = bogieChecksheetSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Bogie checksheet registered successfully!",
            "status": "success",
            "data": response.data,
        })
class bmbcChecksheetViewSet(viewsets.ModelViewSet):
    queryset = bmbcChecksheetForm.objects.all()
    serializer_class = bmbcChecksheetSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "BMBc checksheet registered successfully!",
            "status": "success",
            "data": response.data,
        })