# Third Party Stuff
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin


# Hello-world-app Stuff
from hello_world_app.base import response

from . import models, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated

from hello_world_app.base.api.mixins import MultipleSerializerMixin
class AuthViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):

    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializers.LoginSerializer,
        'logout': serializers.EmptySerializer,
        'password_change': serializers.PasswordChangeSerializer,
        'password_reset': serializers.PasswordResetSerializer,
        'password_reset_confirm': serializers.PasswordResetConfirmSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = services.get_and_authenticate_user(**serializer.validated_data)
        ctx = self.get_serializer_context()
        data = serializers.AuthUserSerializer(user, context=ctx).data
        return response.Ok(data)

    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated,])
    def logout(self, request):
        """
        Calls Django logout method; Does not work for UserTokenAuth.
        """
        logout(request)
        return response.Ok({"success": "Successfully logged out."})

    @action(methods=['POST', ], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return response.NoContent()

    @action(methods=['POST', ], detail=False)
    def password_reset(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = services.get_user_by_email(serializer.data['email'])
        if user:
            services.send_password_reset_mail(user)
        return response.Ok({'message': 'Further instructions will be sent to the email if it exists'})

    @action(methods=['POST', ], detail=False)
    def password_reset_confirm(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = services.get_user_for_password_reset_token(serializer.validated_data['token'])
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return response.NoContent()



class CurrentUserViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.filter(is_active=True)

    def get_object(self):
        return self.request.user

    def list(self, request):
        """Get logged in user profile"""
        serializer = self.get_serializer(self.get_object())
        return response.Ok(serializer.data)

    def partial_update(self, request):
        """Update logged in user profile"""
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Ok(serializer.data)

class UserViewSet(ListModelMixin,
                  RetrieveModelMixin,
                  CreateModelMixin,
                  UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = models.User.objects.select_related('profile').all()
    serializer_class = serializers.UserSerializer
    search_fields = ('^first_name', '^email', '=phone')
    phone_number_field = 'phone'
    default_country_code = '+1'
    ordering = '-date_joined'
