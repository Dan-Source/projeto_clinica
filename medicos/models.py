from datetime import date
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey

class Especialidade(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    
class Medico(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=200)
    email = models.EmailField(verbose_name="Email")
    crm = models.CharField(verbose_name="CRM", max_length=200)
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="O número precisa estar neste formato: \
                    '+99 99 9999-0000'.")

    telefone = models.CharField(verbose_name="Telefone",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
    especialidade = ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='medicos')

def validar_dia(value):
    today = date.today()
    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')

class Agenda(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda')
    dia = models.DateField(help_text="Insira uma data para agenda", validators=[validar_dia])
    
    HORARIOS = (
        ("1", "07:00 ás 08:00"),
        ("2", "08:00 ás 09:00"),
        ("3", "09:00 ás 10:00"),
        ("4", "10:00 ás 11:00"),
        ("5", "11:00 ás 12:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)