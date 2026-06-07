from rest_framework import serializers
from .models import ServiceCategory, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "name_ru",
            "name_ky",
            "description",
            "description_ru",
            "description_ky",
            "image",
            "order",
        )


class ServiceCategorySerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCategory
        fields = ("id", "name", "name_ru", "name_ky", "slug", "services")

    def get_services(self, obj):
        active = obj.services.filter(is_active=True)
        return ServiceSerializer(active, many=True, context=self.context).data