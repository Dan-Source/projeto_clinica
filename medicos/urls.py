from django.urls import path
from . import views

app_name = 'medicos'

urlpatterns = [
    path('registro/', views.medico_cadastro, name='medico-cadastro'),
    path('agendar/', views.agenda_cadastro, name='agenda-cadastro'),
    
]