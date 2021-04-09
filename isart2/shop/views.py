from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


from .models import *


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SubCategory to be viewed.
    """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = None


class AllProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Product to be viewed.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'count']


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Order to be viewed.
    """
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

