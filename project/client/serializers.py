from rest_framework import serializers
from .models import Client
import phonenumbers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    """
    The following function validates if the name is composed by more than one word, so it must be name and surname.
    """
    def validate_name(self, name):
        full_name = name.split(" ")
        if len(full_name) == 1:
            raise serializers.ValidationError("You must type a first name and a second name.")
        return name

    """
    The following function validates if the address is not composed only by numbers.
    """
    def validate_address(self, address):
        is_there_a_letter = any(c.isalpha() for c in address)
        if is_there_a_letter == False:
            raise serializers.ValidationError("Your address must contain letters.")
        return address

    """
    The following function validates if the phone number contains only number and if it is valid and possible.
    """

    def validate_phone(self, phone):
        brazilian_phone = phonenumbers.parse(phone, "BR")
        is_there_a_not_number = phone.isnumeric()
        if is_there_a_not_number == False:
            raise serializers.ValidationError("The phone number must contain only numbers.")
        elif not phonenumbers.is_possible_number(brazilian_phone) and not phonenumbers.is_valid_number(brazilian_phone):
            raise serializers.ValidationError("Type a valid phone number.")
        return phone
