from rest_framework import serializers
from ommm.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = (
            'id',
            'wording',
            'price'
        )
