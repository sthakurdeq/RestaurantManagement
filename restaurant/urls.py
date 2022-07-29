from django.urls import path, include
from restaurant.views import RestuarantViewSet, ItemViewSet, MenuViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

restaurant_list = RestuarantViewSet.as_view({'get': 'list', 'post': 'create'})
restaurant_detail = RestuarantViewSet.as_view({'get': 'retrieve'})


item_list = ItemViewSet.as_view({'get': 'list', 'post': 'create'})
item_detail = ItemViewSet.as_view({'get': 'retrieve'})


menu_list = MenuViewSet.as_view({'get': 'list', 'post': 'create'})
menu_detail = MenuViewSet.as_view({'get': 'retrieve'})

router.register('restaurants', RestuarantViewSet, basename='restaurant')
router.register('restaurants/<str:restaurant_id>/menu', MenuViewSet, basename='menu')
router.register('item', ItemViewSet, basename='item')

urlpatterns = router.urls
