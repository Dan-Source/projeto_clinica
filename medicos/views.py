from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Medico, Agenda

class MedicoCreateView(LoginRequiredMixin ,CreateView):

    model = Medico
    template_name = 'medicos/cadastro.html'
    fields = ['nome', 'crm', 'telefone', 'especilidade']
    success_url = reverse_lazy('index')
    
class AgendaCreateView(LoginRequiredMixin ,CreateView):

    model = Agenda
    template_name = 'medicos/agenda_cadastro.html'
    fields = "__all__"
    success_url = reverse_lazy('index')
    
medico_cadastro = MedicoCreateView.as_view()
agenda_cadastro = AgendaCreateView.as_view()