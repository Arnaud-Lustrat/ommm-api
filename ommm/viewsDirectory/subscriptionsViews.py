from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ommm.models import Subscriptions
from ommm.serializers import SubscriptionsSerializer


class SubscriptionsList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer


class SubscriptionsDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
