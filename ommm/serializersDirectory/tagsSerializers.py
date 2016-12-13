from rest_framework import serializers
from ommm.models import Tags


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('id', 'wording')
