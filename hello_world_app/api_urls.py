# Third Party Stuff
from rest_framework.routers import DefaultRouter

from hello_world_app.secondapp.views import CityViewSet
from hello_world_app.csvupload.views import	PersonViewSet
# Hello-world-app Stuff
from hello_world_app.base.api.routers import SingletonRouter
from hello_world_app.users.api import CurrentUserViewSet, UserViewSet
from hello_world_app.users.auth.api import AuthViewSet
from newappp.views import ListCreatePost
from hello_world_app.fileupload.views import FileViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, basename='auth')
singleton_router.register('me', CurrentUserViewSet, basename='me')
default_router.register('user', UserViewSet, basename = "users")
default_router.register('city', CityViewSet, basename='city')
default_router.register('file', FileViewSet, basename='file')

default_router.register('post',ListCreatePost, basename = "post")
default_router.register('person',PersonViewSet, basename = "person")

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
