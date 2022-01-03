from django.contrib import admin

from medicos.models import Especialidade, Medico

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    
class MedicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'crm', 'telefone',
    ]
    
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)