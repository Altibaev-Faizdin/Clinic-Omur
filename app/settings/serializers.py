from rest_framework import serializers
from .models import ServiceCategory, Service, Specialist


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "description",
            "image",
            "order",
        )


class ServiceCategorySerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCategory
        fields = ("id", "name", "slug", "services")

    def get_services(self, obj):
        active = obj.services.filter(is_active=True)
        return ServiceSerializer(active, many=True, context=self.context).data
    

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ("id", "full_name", "specialization", "experience", "photo", "order")