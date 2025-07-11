# yourapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet,WheelFormViewSet,bogieViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'wheel-forms', WheelFormViewSet)
router.register(r'bogie-forms', bogieViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

      