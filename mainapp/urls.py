
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
     path('shops/near/<latitude>/<longitude>/<distance>/', shops_within_distance, name='shops_near'),
    path('', include(router.urls)),
]
