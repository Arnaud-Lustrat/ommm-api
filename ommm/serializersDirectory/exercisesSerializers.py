from rest_framework import serializers
from ommm.models import Exercises


class ExercisesSerializer(serializers.ModelSerializer):

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
