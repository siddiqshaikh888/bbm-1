from django.urls import path, include

from .views import dashboard, view_application, view_dashboard_product

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('product/<int:product_id>/', view_dashboard_product, name='view_dashboard_product'),
    path('application/<int:application_id>/', view_application, name='view_application'),
]