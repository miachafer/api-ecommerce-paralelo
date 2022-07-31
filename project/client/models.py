from django.db import models
from django.core.validators import RegexValidator

'''
This phone regex validates Brazil's cell phones and landlines.
Both types of phone numbers have an area code of 2 digits.
Cell phone numbers have 9 digits, and always start with 9.
Landlines number have 8 digits, and never start with 9.
'''

PHONE_REGEX = RegexValidator(r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$', 'Enter a phone number in the correct format. Mobile phones: (XX) XXXXX-XXXX Landlines: (XX) XXXX-XXXX')

'''
The primary key of this model is the CPF (Cadastro de Pessoa Física), or the Brazilian equivalent to Social Security Number.
The CPF number is going to be validated by the CPF_REGEX, which validates the format XXX.XXX.XXX-XX
'''

# CPF_REGEX = RegexValidator(r'^[1-9]{3}\.[1-9]{3}\.[1-9]{3}\-[1-9]{2}$', 'Enter your CPF number in the format XXX.XXX.XXX-XX')

class Client(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Full name",
        help_text="Type a name and a surname")
    cpf = models.CharField(
        primary_key=True,
        max_length=14,
        verbose_name="CPF",
        help_text="Type your CPF in the following format: 11122233344",
        )
    address = models.TextField(verbose_name="Address")
    phone = models.CharField(
        max_length=15,
        verbose_name="Phone number",
        help_text="Type phone number in the following format: (XX) XXXXX-XXXX for mobile phones or (XX) XXXX-XXXX for landlines.",
        validators=[PHONE_REGEX],
        unique=True)
    email = models.EmailField(max_length=100, unique=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, CPF: {self.cpf}'
