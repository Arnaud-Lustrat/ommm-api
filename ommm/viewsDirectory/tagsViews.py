from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Tags
from ommm.serializers import TagsSerializer


class TagsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TagsDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)