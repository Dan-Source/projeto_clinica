from django.contrib import admin
from .models import Cliente

    
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'cpf', 'telefone',
    ]
    
admin.site.register(Cliente, ClientAdmin)