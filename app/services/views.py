from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ServiceCategory, Service
from .serializers import ServiceCategorySerializer, ServiceSerializer


class ServiceCategoryListView(ListAPIView):
    serializer_class = ServiceCategorySerializer

    def get_queryset(self):
        return (
            ServiceCategory.objects
            .all()
            .prefetch_related("services")
        )


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer