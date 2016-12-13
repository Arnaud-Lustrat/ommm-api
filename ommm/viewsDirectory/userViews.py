from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import ValidatedUser
from ommm.serializers import ValidatedUserSerializer


class SignUp(mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = ValidatedUser.objects.all()
    serializer_class = ValidatedUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
