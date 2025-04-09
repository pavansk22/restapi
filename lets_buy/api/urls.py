# from django.urls import path
# from product import views
from api import views
from django.urls import path, include

urlpatterns =[
    path("products/",views.ProductsView.as_view(),name="products_view"),
    path("product/<id_arg>",views.ProductView.as_view(),name="products_view")
    
]