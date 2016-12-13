from rest_framework import serializers
from ommm.models import Sessions


class SessionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sessions
        fields = (
            'id',
            'users',
            'exercise',
            'date',
            'heartbeat',
            'feeling'
        )
