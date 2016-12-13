from rest_framework import serializers
from ommm.models import User, ValidatedUser, Tags, Types, Exercises, Subscriptions, Sessions, Favs


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    extra_kwargs = {'password': {'write_only': True}, }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ValidatedUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ValidatedUser
        fields = (
            'relationship',
            'user'
        )

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User(email=user_data['email'], username=user_data['username'])
        user.set_password(user_data['password'])
        user.save()

        validated_user = ValidatedUser.objects.create(user=user, **validated_data)
        return validated_user


class TypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Types
        fields = ('id', 'wording', 'animation_name')


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('id', 'wording')


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


class SubscriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = (
            'id',
            'wording',
            'price'
        )


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


class FavsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favs
        fields = (
            'id',
            'users',
            'fav'
        )
