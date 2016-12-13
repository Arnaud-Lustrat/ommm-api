from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Exercises
from ommm.serializers import ExercisesSerializer


class ExercisesList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExercisesDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)