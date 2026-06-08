from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from app.settings import translation
from .models import ServiceCategory, Service, Specialist


class ServiceInline(TranslationTabularInline):
    model = Service
    extra = 0


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TabbedTranslationAdmin):
    list_display = ("name", "slug", "order")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ("name", "category", "is_active", "order", "created_at")
    list_filter = ("category", "is_active")
    list_editable = ("is_active", "order")
    search_fields = ("name",)
    readonly_fields = ("created_at",)


@admin.register(Specialist)
class SpecialistAdmin(TabbedTranslationAdmin):
    list_display = ("full_name", "specialization", "experience", "is_active", "order")
    list_filter = ("is_active",)
    list_editable = ("is_active", "order")
    search_fields = ("full_name", "specialization")