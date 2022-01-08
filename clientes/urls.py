from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registro/', views.cliente_cadastro, name='cliente_cadastro'),
    path('cliente/atualizar/', views.cliente_atualizar, name='cliente_atualizar')
]