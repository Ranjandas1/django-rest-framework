# yourapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet,WheelFormViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'wheel-forms', WheelFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

      