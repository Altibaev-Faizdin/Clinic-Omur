from modeltranslation.translator import register, TranslationOptions
from .models import ServiceCategory, Service


@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description")