from rest_framework import serializers
from ommm.models import Types, Exercises

# from .exercisesSerializers import ExercicesWithoutTypeSerializer


class TypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Types
        fields = ('id', 'wording', 'animation_name')


# class ListTypesSerializer(serializers.ModelSerializer):
#     type_exercises = ExercicesWithoutTypeSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Types
#         fields = ('id', 'wording', 'type_exercises')
