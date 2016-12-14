from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import ValidatedUser
from ommm.serializers import ValidatedUserSerializer, UserExercicesFavSerializer


class SignUp(generics.CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = ValidatedUser.objects.all()
    serializer_class = ValidatedUserSerializer


class Profile(generics.GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = ValidatedUserSerializer

    def get(self, request, *args, **kwargs):
        pk = request.user.id
        user = ValidatedUser.objects.get(pk=pk)

        serializer = ValidatedUserSerializer(user)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = request.user.id
        validated_user = ValidatedUser.objects.get(pk=pk)

        serializer = ValidatedUserSerializer(validated_user)
        serializer.update(validated_user, request.data)

        return Response(serializer.data)
