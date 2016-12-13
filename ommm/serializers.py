from rest_framework import serializers
from ommm.models import *


# Import serializers

from ommm.serializersDirectory.usersSerializers import *
from ommm.serializersDirectory.typesSerializers import *
from ommm.serializersDirectory.tagsSerializers import *
from ommm.serializersDirectory.exercisesSerializers import *
from ommm.serializersDirectory.subscriptionsSerializers import *
from ommm.serializersDirectory.sessionsSerializers import *
from ommm.serializersDirectory.favsSerializers import *


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#     extra_kwargs = {'password': {'write_only': True}, }
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
#
#
# class ValidatedUserSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#
#     class Meta:
#         model = ValidatedUser
#         fields = (
#             'relationship',
#             'user'
#         )
#
#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#
#         user = User(email=user_data['email'], username=user_data['username'])
#         user.set_password(user_data['password'])
#         user.save()
#
#         validated_user = ValidatedUser.objects.create(user=user, **validated_data)
#         return validated_user
