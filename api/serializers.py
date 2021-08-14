from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,allow_empty_file=False) 

    class Meta:
        model = Product
        fields ="__all__"