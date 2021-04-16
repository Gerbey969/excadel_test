import json

from django.shortcuts import render
from .models import *
from .forms import *
from .serializers import *
import urllib.parse
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

class RestaurantAPIView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializers = RestaurantSerializer(restaurants, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        print("Request Data", request.data)
        data = request.data
        restaurant = Restaurant.objects.create(name=data["name"], rank=data["rank"], average_bill=data["average_bill"])
        restaurant.save()
        for product in data["menu"]:
            product_obj = Products.objects.get(title=product["title"])
            restaurant.menu.add(product_obj)

        serializer = RestaurantSerializer(restaurant)

        return Response(serializer.data)

class FiltertedView(APIView):

    def get(self, request):
        form = ProductSearchForm(request.GET)

        if not form.is_valid():
            raise Http404()

        product_name = form.cleaned_data['itemName']
        products = Restaurant.objects.filter(menu__title=product_name)
        filtered_ser = RestaurantSerializer(products, many=True)

        return Response(filtered_ser.data)


class SortedView(APIView):

    def get(self, request):

        restaraunts = Restaurant.objects.all().order_by('-rank')
        serializer = RestaurantSerializer(restaraunts, many=True)

        return Response(serializer.data)

class LuxuryView(APIView):

    def get(self, request):

        restaraunts = Restaurant.objects.all().order_by('-average_bill')
        serializer = RestaurantSerializer(restaraunts, many=True)

        return Response(serializer.data)
