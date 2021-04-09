from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'id']


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name', 'id']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.ReadOnlyField(source='subcategory.name')
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'name', 'description', 'price', 'count']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'product']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product']

