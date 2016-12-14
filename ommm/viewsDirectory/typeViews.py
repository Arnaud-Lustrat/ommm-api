from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Types
from ommm.serializers import TypesSerializer


class TypesList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Types.objects.all()
    serializer_class = TypesSerializer


class TypesDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
