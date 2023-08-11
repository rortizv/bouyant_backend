from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'doc_type', 'doc_number', 'address', 'country', 'born_date', 'password']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'email': instance.email,
            'username': instance.username,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'phone_number': instance.phone_number,
            'doc_type': instance.doc_type,
            'doc_number': instance.doc_number,
            'address': instance.address,
            'country': instance.country,
            'born_date': instance.born_date,
            'password': instance.password
        }



class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'admin' in value.lower():
            raise serializers.ValidationError('Cannot exist a user with admin as name')
        return value

    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('Email cannot be empty')

        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance