from django_filters import rest_framework
from .models import *


class ProductFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name='price', lookup_expr='lte')
    min_count = rest_framework.NumberFilter(field_name='count', lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'min_price', 'max_price', 'min_count']

