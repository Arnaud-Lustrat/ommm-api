from rest_framework import serializers
from ommm.models import Types


class TypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Types
        fields = ('id', 'wording', 'animation_name')
