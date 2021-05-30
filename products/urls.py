from django.urls import path

from products.views import (
        product_detail_view
        , product_create_view
        , render_initial_data
        , dynamic_lookup_view
        , product_delete_view
        , product_list_view
    )

app_name = 'products'
urlpatterns = [
    #path('product/', product_detail_view, name='product_detail_view'),
    path('', product_list_view, name='product_list'),
    path('<int:my_id>/', dynamic_lookup_view, name='product_dynamic'),

    path('create/', product_create_view, name='product_create'),
    path('render/', render_initial_data, name='render_data'),
    path('<int:my_id>/delete/', product_delete_view, name='product_delete'),


]


    