from django.urls import path
from . import views

urlpatterns = [
    path("services/", views.ServiceCategoryListView.as_view(), name="service-list"),
    path("services/<int:pk>/", views.ServiceDetailView.as_view(), name="service-detail"),
]