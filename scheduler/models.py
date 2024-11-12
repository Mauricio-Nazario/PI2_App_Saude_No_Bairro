from django.db import models
from django.core.exceptions import ValidationError
import re

# Função de Validação de CPF
def validar_cpf(value):
    cpf = re.sub(r'[^0-9]', '', value)  # Remove tudo que não for número
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError('CPF inválido')

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf])
    ubs = models.CharField(max_length=100)  # Unidade Básica de Saúde
    anamnese = models.TextField()  # Dados de saúde preenchidos pelo médico

    def __str__(self):
        return self.nome_completo

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField()
    encaminhamento = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.paciente.nome_completo} - {self.data_agendamento}"

