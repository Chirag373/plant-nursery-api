from django.urls import path
from .views import PlantAPI

urlpatterns = [
    path("plants", PlantAPI.as_view(), name="plant"),
    path("plant/<int:pk>", PlantAPI.as_view(), name="water-plant"),
    path("plant/<int:pk>/water", PlantAPI.as_view(), name="water-plant"),
]