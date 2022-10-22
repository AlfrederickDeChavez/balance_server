from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email' , 'age', 'gender', 'height', 'weight']


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'age', 'gender', 'height', 'weight']

    def update(self, instance, validated_data):

        instance.username = validated_data['username']
        instance.age = validated_data['age']
        instance.gender = validated_data['gender']
        instance.height = validated_data['height']
        instance.weight = validated_data['weight']

        instance.save()

        return instance