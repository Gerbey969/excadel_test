from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404


class ProductRelatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ("title", )


class RestaurantSerializer(serializers.ModelSerializer):

    menu = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Restaurant
        fields = ['name', "rank", "average_bill", "menu"]
        depth = 1
