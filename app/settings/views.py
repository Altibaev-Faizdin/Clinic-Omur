from rest_framework import mixins, viewsets
from .models import ServiceCategory, Service
from .serializers import ServiceCategorySerializer, ServiceSerializer


class ServiceCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ServiceCategorySerializer
    queryset = ServiceCategory.objects.all().prefetch_related("services")


class ServiceViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer