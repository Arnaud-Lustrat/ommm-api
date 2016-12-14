from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Tags
from ommm.serializers import TagsSerializer


class TagsList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class TagsDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
