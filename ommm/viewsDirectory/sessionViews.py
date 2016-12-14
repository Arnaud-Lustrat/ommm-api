from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Sessions
from ommm.serializers import SessionsSerializer


class SessionsList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer


class SessionsDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer
