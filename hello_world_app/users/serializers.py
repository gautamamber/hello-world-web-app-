from rest_framework import serializers

from . import models

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = ['id', 'gender', 'date_of_birth']


class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(required=False)
	class Meta:
		model = models.User
		fields = ['id', 'first_name', 'last_name', 'email', 'role', 'profile']

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)

class EmptySerializer(serializers.Serializer):
    pass


class AuthUserSerializer(UserSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ['auth_token']

    def get_auth_token(self, obj):
        return auth_services.get_token_for_user(obj, self.context['request'])

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    default_error_messages = {
        'invalid_password': 'Current password does not match'
    }

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(self.default_error_messages['invalid_password'])
        return value

    def validate_new_password(self, value):
        # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#django.contrib.auth.password_validation.validate_password
        password_validation.validate_password(value)
        return value

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value