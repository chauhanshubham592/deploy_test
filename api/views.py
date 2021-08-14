from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

def myHome(request):
    return HttpResponse("<h1>Home Page</h1>")

def myApi(request):
    return JsonResponse({"data":"hello"})

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer