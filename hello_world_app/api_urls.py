# Third Party Stuff
from rest_framework.routers import DefaultRouter

from hello_world_app.secondapp.views import CityViewSet
# Hello-world-app Stuff
from hello_world_app.base.api.routers import SingletonRouter
from hello_world_app.users.api import CurrentUserViewSet
from hello_world_app.users.auth.api import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, basename='auth')
singleton_router.register('me', CurrentUserViewSet, basename='me')
default_router.register('city', CityViewSet, basename='post')
# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
