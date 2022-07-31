from rest_framework.routers import DefaultRouter

from restaurant.views import (ItemViewSet, MenuViewSet, RatingViewSet,
                              RestuarantViewSet, ResultViewSet,
                              TodayMenuViewSet)

router = DefaultRouter()

# restaurant api
restaurant_list = RestuarantViewSet.as_view({"get": "list", "post": "create"})
restaurant_detail = RestuarantViewSet.as_view({"get": "retrieve"})

# items api
item_list = ItemViewSet.as_view({"get": "list", "post": "create"})
item_detail = ItemViewSet.as_view({"get": "retrieve"})

# menu api
menu_list = MenuViewSet.as_view({"get": "list", "post": "create"})
menu_detail = MenuViewSet.as_view({"get": "retrieve"})

# rating api
rating_list = RatingViewSet.as_view({"get": "list", "post": "create"})
rating_detail = RatingViewSet.as_view({"get": "retrieve"})

# todays menu list api
today_menu_list = TodayMenuViewSet.as_view({"get": "list"})
result_list = ResultViewSet.as_view({"get": "list"})

router.register("restaurants", RestuarantViewSet, basename="restaurant")
router.register("menu", MenuViewSet, basename="menu")
router.register("item", ItemViewSet, basename="item")
router.register("rating", RatingViewSet, basename="rating")
router.register("today_menu", TodayMenuViewSet, basename="today_menu")
router.register("result", ResultViewSet, basename="result")

urlpatterns = router.urls
