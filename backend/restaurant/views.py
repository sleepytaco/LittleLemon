from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .models import MenuItem, Booking
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     item = get_list_or_404(MenuItem)
    #     serializer = MenuItemSerializer(item, many=True)  
    #     return Response(serializer.data)    
    
    # def post(self, request, *args, **kwargs):
    #     return Response('Menu Item POST response')   
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    # def get(self, request, pk, *args, **kwargs):
    #     item = get_object_or_404(MenuItem, pk=pk)
    #     serializer = MenuItemSerializer(item)  
    #     return Response(serializer.data)
    
    # def put(self, request, *args, **kwargs):
    #     return Response('Single Menu Item PUT response')   
    
    # def delete(self, request, *args, **kwargs):
    #     return Response('Single Menu Item DELETE response')    