from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import ServiceCategory, Service


class ServiceInline(TranslationTabularInline):  
    model = Service
    extra = 0


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TranslationAdmin):  
    list_display = ("name", "slug", "order")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ServiceInline]


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):  
    list_display = ("name", "category", "is_active", "order", "created_at")
    list_filter = ("category", "is_active")
    list_editable = ("is_active", "order")
    search_fields = ("name",)
    readonly_fields = ("created_at",)