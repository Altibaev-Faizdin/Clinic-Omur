from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("services", views.ServiceCategoryViewSet, basename="service-category")
router.register("services-detail", views.ServiceViewSet, basename="service")

urlpatterns = router.urls