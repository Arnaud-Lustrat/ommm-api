from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Favs
from ommm.serializers import FavsSerializer


class FavsList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Favs.objects.all()
    serializer_class = FavsSerializer


class FavsDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Favs.objects.all()
    serializer_class = FavsSerializer
