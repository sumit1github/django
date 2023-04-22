    path('productcatalog/<str:quote_id>/<str:node>/', ProductCatalogue.as_view(), name="productcatalog"),
    path('product_search/', ProductSearchAjax.as_view(), name="product_search" ),