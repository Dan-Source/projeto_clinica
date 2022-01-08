from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Medico, Agenda, Especialidade

class MedicoCreateView(LoginRequiredMixin ,CreateView):

    model = Medico
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome', 'crm', 'telefone', 'especialidade']
    success_url = reverse_lazy('index')
    
class EspecialidadeCreateView(LoginRequiredMixin ,CreateView):

    model = Especialidade
    login_url = 'accounts:login'
    template_name = 'medicos/cadastro.html'
    fields = ['nome',]
    success_url = reverse_lazy('index')


class AgendaCreateView(LoginRequiredMixin ,CreateView):

    model = Agenda
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_cadastro.html'
    fields = ['medico', 'dia', 'horario']
    success_url = reverse_lazy('medicos:agenda_lista')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AgendaListView(LoginRequiredMixin, ListView):
    
    login_url = 'accounts:login'
    template_name = 'medicos/agenda_list.html'

    def get_queryset(self):
        return Agenda.objects.filter(user=self.request.user).order_by('-pk')
    
medico_cadastro = MedicoCreateView.as_view()
especialidade_cadastro = EspecialidadeCreateView.as_view()
agenda_cadastro = AgendaCreateView.as_view()
agenda_lista = AgendaListView.as_view()
