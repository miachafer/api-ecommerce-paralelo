from django.db import models
from localflavor.br.models import BRCPFField

"""
The primary key of this model is the CPF (Cadastro de Pessoa Física), or the Brazilian equivalent to Social Security Number.
The CPF number is going to be validated by the library django-localflavor.
"""

class Client(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Full name",
        help_text="Type a name and a surname")
    cpf = BRCPFField( 
        max_length=11,
        verbose_name="CPF", 
        primary_key=True, 
        help_text="Type your CPF in the following format: 11122233344")
    address = models.TextField(verbose_name="Address")
    phone = models.CharField(
        max_length=11,
        verbose_name="Phone number",
        help_text="Type phone number in the following format: DDD (2 digits) + number (8 or 9 digits) with no spaces")
    email = models.EmailField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Client: {self.name} - CPF: {self.cpf}"
