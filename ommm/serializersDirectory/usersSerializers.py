from rest_framework import serializers
from ommm.models import User, ValidatedUser, Exercises

from .exercisesSerializers import ExercisesSerializer


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
            'housing',
            'weight',
            'card_number',
            'health_level',
            'user'
        )

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User(email=user_data['email'], username=user_data['username'])
        user.set_password(user_data['password'])
        user.save()

        validated_user = ValidatedUser.objects.create(user=user, **validated_data)
        return validated_user

    def update(self, validated_user, validated_data):
        user_data = validated_data.pop('user')

        user = validated_user.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.save()

        validated_user.relationship = validated_data.get('relationship', validated_user.relationship)
        validated_user.housing = validated_data.get('housing', validated_user.housing)
        validated_user.weight = validated_data.get('weight', validated_user.weight)
        validated_user.card_number = validated_data.get('card_number', validated_user.card_number)
        validated_user.health_level = validated_data.get('health_level', validated_user.health_level)

        validated_user.save()

        return validated_user


class UserExercicesFavSerializer(serializers.ModelSerializer):
    user_favs = ExercisesSerializer(many=True, read_only=True)

    class Meta:
        model = ValidatedUser
        fields = (
            'housing',
            'user_favs'
        )

    def add_new_fav(self, validated_user, validated_data):

        exercies = validated_data.pop('exercices')

        for exo in exercies:
            exercies = Exercises.objects.get(pk=exo.pop('id'))
            validated_user.user_favs.add(exercies)

        return validated_user
