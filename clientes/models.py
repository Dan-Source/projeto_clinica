from django_cpf_cnpj.fields import CPFField
from django.core.validators import RegexValidator
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    email = models.EmailField(verbose_name="Email")
    SEXO = (
        ("MAS", "Maculino"),
        ("FEM", "Feminino")
    )
    
    sexo = models.CharField(max_length=9, choices=SEXO,)
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número precisa estar neste formato: \
                        '+99 99 9999-0000'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    cpf = CPFField(verbose_name="CPF",
                    max_length=50,
                    unique=True,)
