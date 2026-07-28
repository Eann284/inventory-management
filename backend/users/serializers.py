from rest_framework import serializers
from .models import UserManagerModel

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserManagerModel
        fields = ['uid', 'name', 'email', 'role', 'area', 'stock', 'password']
        read_only_fields= ['uid']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = UserManagerModel.objects.create(**validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

