from rest_framework.response import Response

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Exercises, ValidatedUser
from ommm.serializers import ExercisesSerializer, UserExercicesFavSerializer


class ExercisesList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer


class ExercisesDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer


class Fav(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = ValidatedUser.objects.all()
    serializer_class = UserExercicesFavSerializer


# class List(generics.ListAPIView):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Exercises.objects.all()
#     serializer_class = ExercisesSerializer


class List(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserExercicesFavSerializer

    def get(self, request, *args, **kwargs):
        exercices = Exercises.objects.all()
        serializer = ExercisesSerializer(exercices, many=True)

        good_data = rewrite_data(serializer.data)
        return Response(good_data)
        #return Response(serializer.data)


class Favoris(generics.GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserExercicesFavSerializer

    def get(self, request, *args, **kwargs):
        user_pk = request.user.id
        validated_user = ValidatedUser.objects.get(pk=user_pk)
        serializer = UserExercicesFavSerializer(validated_user)

        good_data = rewrite_data(serializer.data)
        return Response(good_data)

    def post(self, request, *args, **kwargs):
        user_pk = request.user.id
        validated_user = ValidatedUser.objects.get(pk=user_pk)

        serializer = UserExercicesFavSerializer(validated_user)
        serializer.add_new_fav(validated_user, request.data)

        good_data = rewrite_data(serializer.data)
        return Response(good_data)
        #return Response(serializer.data)


def rewrite_data(validated_data):

    if "user_favs" in validated_data:
        validated_data = validated_data.pop('user_favs')

    list_tag = []
    list_tag_id = []

    for exo in validated_data:

        tag = exo.pop('tag')
        tag_id = tag['id']

        if tag_id in list_tag_id:
            tag_index = list_tag_id.index(tag_id)
            list_tag[tag_index]['exercises'].append(exo)
        else:
            tag.update({'exercises': []})
            list_tag.append(tag)
            list_tag_id.append(tag_id)
            tag_index = list_tag_id.index(tag_id)
            list_tag[tag_index]['exercises'].append(exo)

        # if tag in list_tag:
        #     tag_index = list_tag.index(tag)
        #     list_tag[tag_index]['exercises'].append(exo)
        # else:
        #     tag.update({'exercises': []})
        #     list_tag.append(tag)
        #     tag_index = list_tag.index(tag)
        #     list_tag[tag_index]['exercises'].append(exo)

    return list_tag
