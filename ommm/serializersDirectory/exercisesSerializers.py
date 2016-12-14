from rest_framework import serializers
from ommm.models import Exercises
from .typesSerializers import TypesSerializer
from .tagsSerializers import TagsSerializer


class ExercisesSerializer(serializers.ModelSerializer):
    type = TypesSerializer(read_only=True)
    tag = TagsSerializer(read_only=True)

    class Meta:
        model = Exercises
        fields = (
            'id',
            'source',
            'total_session_count',
            'total_fav',
            'created_at',
            'updated_at',
            'type',
            'tag'
        )


class ExercicesWithoutTypeSerializer(serializers.ModelSerializer):
    tag = TagsSerializer(read_only=True)

    class Meta:
        model = Exercises
        fields = (
            'id',
            'source',
            'total_session_count',
            'total_fav',
            'created_at',
            'updated_at',
            'tag'
        )
