from django.urls import path, include

from .api import api_search 
from .views import add_product, product_detail, apply_for_product, search_p, edit_product #, delete_view

urlpatterns = [
    path('api/search/', api_search, name='api_search'),
    path('search_p/', search_p, name='search-p'),
    path('add/', add_product, name='add_product'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('<int:product_id>/edit/', edit_product, name='edit_product'),
    path('<int:product_id>/apply_for_product/', apply_for_product, name='apply_for_product'),
    #path('<id>/delete', delete_view ),
]