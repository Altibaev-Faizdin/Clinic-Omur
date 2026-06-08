from rest_framework import mixins, viewsets
from .models import ServiceCategory, Service, Specialist
from .serializers import ServiceCategorySerializer, ServiceSerializer, SpecialistSerializer




class ServiceCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ServiceCategorySerializer
    queryset = ServiceCategory.objects.all().prefetch_related("services")





class ServiceViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer





class SpecialistViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Specialist.objects.filter(is_active=True)
    serializer_class = SpecialistSerializer