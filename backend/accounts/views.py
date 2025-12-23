from django.shortcuts import render
from .models import WatchList
from rest_framework  import generics
from .serializer import WatchListSerializer
from rest_framework import permissions
# Create your views here.


class WatchListListCreateAPI(generics.ListCreateAPIView):
        queryset = WatchList.objects.all()
        serializer_class = WatchListSerializer
        permission_classes = [permissions.IsAuthenticated]
        def perform_create(self,serializer):
                serializer.save(user=self.request.user)