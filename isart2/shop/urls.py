from django.urls import path

from . import views

urlpatterns = [
   #path('categories/', views.CategoryViewSet.as_view({'get': 'list'})),
   #path('subcategories/', views.SubCategoryViewSet.as_view({'get': 'list'})),
   #path('orders/', views.OrderViewSet.as_view({'get': 'list'})),
   #path('products/', views.ProductViewSet.as_view({'get': 'list'})),
    path('allproducts/', views.AllProductViewSet.as_view({'get': 'list'})),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
