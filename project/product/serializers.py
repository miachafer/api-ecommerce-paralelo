from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    """
    The following functions validate if the product's name and description contains letters. If the name and/or description don't contain letter, these function will raise an error.
    """
    def validate_name(self, name):
        is_there_a_letter = any(c.isalpha() for c in name)
        if is_there_a_letter == False:
            raise serializers.ValidationError("The product's name must contain letters.")
        return name
    
    def validate_description(self, description):
        is_there_a_letter = any(c.isalpha() for c in description)
        if is_there_a_letter == False:
            raise serializers.ValidationError("The product's description must contain letters.")
        return description
        