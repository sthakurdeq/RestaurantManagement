from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()

user_list = UserViewSet.as_view({"post": "create", "get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})

router.register("", UserViewSet, basename="user")
urlpatterns = router.urls
