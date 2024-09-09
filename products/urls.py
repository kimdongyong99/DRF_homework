from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductListAPIView.as_view(), name="product_list"),
    path("", views.ProductCreateAPIView.as_view(), name="product_create"),
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
]
