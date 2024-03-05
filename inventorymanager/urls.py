from rest_framework import routers

from inventorymanager.views import EstablishmentViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"establishments", EstablishmentViewSet)
urlpatterns = router.urls
