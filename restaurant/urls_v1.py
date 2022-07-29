from restaurant.views import RatingViewSet, RestuarantViewSet, ItemViewSet, MenuViewSet, TodayMenuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# restaurant api
restaurant_list = RestuarantViewSet.as_view({'get': 'list', 'post': 'create'})
restaurant_detail = RestuarantViewSet.as_view({'get': 'retrieve'})

# items api
item_list = ItemViewSet.as_view({'get': 'list', 'post': 'create'})
item_detail = ItemViewSet.as_view({'get': 'retrieve'})

# menu api
menu_list = MenuViewSet.as_view({'get': 'list', 'post': 'create'})
menu_detail = MenuViewSet.as_view({'get': 'retrieve'})

# rating api
rating_list = RatingViewSet.as_view({'get': 'list', 'post': 'create'})
rating_detail = RatingViewSet.as_view({'get': 'retrieve'})

# todays menu list api
today_menu_list = TodayMenuViewSet.as_view({'get': 'list'})

router.register('restaurants', RestuarantViewSet, basename='restaurant')
router.register('menu', MenuViewSet, basename='menu')
router.register('item', ItemViewSet, basename='item')
router.register('rating', RatingViewSet, basename='rating')
router.register('today_menu', TodayMenuViewSet, basename='today_menu')

urlpatterns = router.urls
