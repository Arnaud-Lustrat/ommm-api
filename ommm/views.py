from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from ommm.models import ValidatedUser, Types, Tags, Exercises, Subscriptions, Sessions, Favs
from ommm.serializers import ValidatedUserSerializer, TypesSerializer, TagsSerializer, ExercisesSerializer, \
    SubscriptionsSerializer, SessionsSerializer, FavsSerializer

from rest_framework import mixins
from rest_framework import generics

from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


# Import all models views

#from ommm.viewsDirectory.userViews import SignUp, Home
#from ommm.viewsDirectory.favsViews import FavsList, FavsDetail
#from ommm.viewsDirectory.exercisesViews import ExercisesList, ExercisesDetail
#from ommm.viewsDirectory.sessionViews import SessionsList, SessionsDetail
#from ommm.viewsDirectory.subscriptionsViews import SubscriptionsList, SubscriptionsDetail
#from ommm.viewsDirectory.tagsViews import TagsList, TagsDetail
#from ommm.viewsDirectory.typeViews import TypesList, TypesDetail

from ommm.viewsDirectory.userViews import *
from ommm.viewsDirectory.favsViews import *
from ommm.viewsDirectory.exercisesViews import *
from ommm.viewsDirectory.sessionViews import *
from ommm.viewsDirectory.subscriptionsViews import *
from ommm.viewsDirectory.tagsViews import *
from ommm.viewsDirectory.typeViews import *


# class SignUp(APIView):
#
#     def post(self, request):
#         serializer = ValidatedUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
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


# class TypesList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Types.objects.all()
#     serializer_class = TypesSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class TypesDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     #permission_classes = (IsAuthenticated,)
#     queryset = Types.objects.all()
#     serializer_class = TypesSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class TagsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     #permission_classes = (IsAuthenticated,)
#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class TagsDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class ExercisesList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     #permission_classes = (IsAuthenticated,)
#     queryset = Exercises.objects.all()
#     serializer_class = ExercisesSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ExercisesDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Exercises.objects.all()
#     serializer_class = ExercisesSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class SubscriptionsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Subscriptions.objects.all()
#     serializer_class = SubscriptionsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SubscriptionsDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Subscriptions.objects.all()
#     serializer_class = SubscriptionsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class SessionsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Sessions.objects.all()
#     serializer_class = SessionsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SessionsDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Sessions.objects.all()
#     serializer_class = SessionsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class FavsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Favs.objects.all()
#     serializer_class = FavsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class FavsDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Favs.objects.all()
#     serializer_class = FavsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# the documentation view
class SwaggerSchemaView(APIView):
    renderer_classes = [OpenAPIRenderer, SwaggerUIRenderer]

    def get(self, request):

        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)
