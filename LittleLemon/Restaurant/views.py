from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer


class bookingview(APIView):

    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    

class menuview(APIView):
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data = request.data)
        

        if serializer.is_valid():
            serializer.save()
            return Response({'status': "success", "data": serializer.data})