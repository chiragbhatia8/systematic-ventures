from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import Role

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description', 'permissions')

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_staff', 'role')


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)
    is_staff = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
