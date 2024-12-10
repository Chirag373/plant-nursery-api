from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PlantSerializer
from rest_framework import status
from api.models import Plant
from django.shortcuts import get_object_or_404
from datetime import datetime, timezone

# Create your views here.
class PlantAPI(APIView):
    # plant a seed
    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # check the status of the plant or all plants at once
    def get(self, request, pk=None):
        if pk:
            plant = get_object_or_404(Plant, pk=pk)
            serializer = PlantSerializer(plant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            plants = Plant.objects.all()
            serializer = PlantSerializer(plants, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    # water a plant the water date and health by 1% would updated
    def put(self, request, pk=None):
        if pk:
            plant = get_object_or_404(Plant, pk=pk)
            plant.last_watered_date = datetime.now()
            if 0 < plant.health < 100:
                plant.health += 1
            plant.save()
            serializer = PlantSerializer(plant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"data not updated"}, status=status.HTTP_304_NOT_MODIFIED)

    