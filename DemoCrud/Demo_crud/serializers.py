from rest_framework import serializers
from .models import User, Rol, UserRol
# Serializador para los usuarios:
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    class RoleUserSerializer(serializers.Serializer):
        role = serializers.CharField(allow_null=False, allow_blank=False)

    class RolSerializer(serializers.ModelSerializer):
        class Meta:
            model = Rol
            fields = '__all__'