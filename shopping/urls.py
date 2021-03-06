from django.urls import include, path
from rest_framework import routers
from shopping.views import ShoppingItemViewSet

routers = router.DefaultRouter()
router.register(
    'shopping-item', ShoppingItemViewSet, base_name='shopping-item'
)


urlpatterns = [
    ...
    path('', include(router.urls)),
]