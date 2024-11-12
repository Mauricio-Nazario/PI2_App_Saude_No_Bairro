from django.shortcuts import render, redirect
from .models import Paciente, Agendamento
from .forms import PacienteForm, AgendamentoForm

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'scheduler/lista_pacientes.html', {'pacientes': pacientes})

def criar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'scheduler/criar_paciente.html', {'form': form})

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'scheduler/lista_agendamentos.html', {'agendamentos': agendamentos})

def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'scheduler/criar_agendamento.html', {'form': form})

