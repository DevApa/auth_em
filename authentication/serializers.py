from rest_framework import serializers

from entrepreneur.models import Usuario


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['last_login', 'is_superuser', 'is_admin', 'created_at', 'updated_at', 'groups', 'user_permissions', 'is_active', 'is_evaluator']

    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name')
