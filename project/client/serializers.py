from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    """
    This function validates if the name is composed by more than one word, so it must be name and surname.
    """
    def validate_name(self, name):
        full_name = name.split(" ")
        if len(full_name) == 1:
            raise serializers.ValidationError("You must type a first name and a second name.")
        return name

    """
    This function validates if the address is not composed only by numbers.
    """
    def validate_address(self, address):
        is_there_a_letter = any(c.isalpha() for c in address)
        if is_there_a_letter == False:
            raise serializers.ValidationError("Your address must contain letters.")
        return address
