from django.urls  import path
from products.views import (
    product_list_view,
    product_add_view,
    product_remove_view,
    dynamic_detail_view
)


app_name = 'products' # namespace
urlpatterns = [
    path('',product_list_view,name='about-product'),
    path('list/',product_list_view,name='list-products'),
    path('add/',product_add_view,name='add-product'),
    path('<int:product_id>/remove/',product_remove_view, name='remove-product'), # '/' syntacticaly means the end of an URL
    path('<int:product_id>/details',dynamic_detail_view,name='product-details'),
]
