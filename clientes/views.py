from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente

class ClienteCreateView(LoginRequiredMixin ,CreateView):
    
    model = Cliente
    template_name = 'clientes/cadastro.html'
    fields = ['nome', 'email', 'sexo', 'telefone', 'cpf']
    success_url = reverse_lazy('index')
    
cliente_cadastro = ClienteCreateView.as_view()