from django.urls import include, path
from products.views import product_create_view, product_show_view, product_delete_view, product_edit_view, product_index_view

app_name = 'products'
urlpatterns = [
    path('', product_index_view, name="product-index"),
    path('create/', product_create_view, name="product-create"),
    path('<int:p_id>/', product_show_view, name="product-show"),
    path('<int:p_id>/delete/', product_delete_view, name="product-delete"),
    path('<int:p_id>/edit/', product_edit_view, name="product-edit"),
]
