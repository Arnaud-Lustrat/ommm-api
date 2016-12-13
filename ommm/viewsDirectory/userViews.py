# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import ValidatedUser
from ommm.serializers import ValidatedUserSerializer


# class SignUp(APIView):
#
#     def post(self, request):
#         serializer = ValidatedUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUp(mixins.CreateModelMixin, generics.GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = ValidatedUser.objects.all()
    serializer_class = ValidatedUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class Home(APIView):
#     #permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         data = {
#             'status': 'request was permitted',
#             'id': request.user.id,
#             'username': request.user.username,
#             'token': str(request.auth)
#         }
#
#         return Response(data, status=status.HTTP_200_OK)