from django import forms
from .models import Paciente, Agendamento

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome_completo', 'data_nascimento', 'endereco', 'telefone', 'cpf', 'ubs', 'anamnese']

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['paciente', 'data_agendamento', 'encaminhamento', 'descricao']

