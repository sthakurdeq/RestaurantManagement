from django.urls import include, path
from rest_framework.routers import DefaultRouter

from restaurant.views_v2 import RatingV2ViewSet

router = DefaultRouter()
rating_v2_list = RatingV2ViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = []

router.register("rating", RatingV2ViewSet, basename="ratingv2")

urlpatterns = router.urls
