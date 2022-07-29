from django.urls import path
from .views import UserViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# user = UserViewSet.as_view({'post': 'create'})
urlpatterns = [

   path('create', UserViewSet.as_view({'post': 'create'})),
]

# router.register('item', UserViewSet, basename='user')
# urlpatterns = router.urls