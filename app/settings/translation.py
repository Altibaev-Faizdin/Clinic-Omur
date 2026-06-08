from modeltranslation.translator import register, TranslationOptions
from .models import ServiceCategory, Service, Specialist


@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description")

@register(Specialist)
class SpecialistTranslationOptions(TranslationOptions):
    fields = ("full_name", "specialization")