from django.shortcuts import render, redirect
from .models import Participantes, Elementos
from .forms import ElementosForm, ParticipantesForm

# Create your views here.
def home(request):
    return render(request, "app/home.html")

def consulta_participantes(request):
    participantes = Participantes.objects.all()
    return render(request, "app/consulta_participantes.html", {'participantes': participantes})

def consulta_elementos(request):
    elementos = Elementos.objects.all()
    return render(request, "app/consulta_elementos.html", {'elementos': elementos})

def editar_elementos(request, id):
    elementos = Elementos.objects.get(id_elemento=id)
    formulario = ElementosForm(request.POST or None, request.FILES or None, instance = elementos)
    if formulario.is_valid():
        formulario.save()
        return redirect(consulta_elementos)
    return render(request, "app/editar_elementos.html", {'elementos': formulario})

def editar_participantes(request, id):
    participantes = Participantes.objects.get(id_participante=id)
    formulario = ParticipantesForm(request.POST or None, request.FILES or None, instance = participantes)
    if formulario.is_valid():
        formulario.save()
        return redirect(consulta_participantes)
    return render(request, "app/editar_participantes.html", {'participantes': formulario})

def alta_elementos(request):
    elementos = ElementosForm(request.POST or None, request.FILES or None)
    if elementos.is_valid():
        elementos.save()
        return redirect(consulta_elementos)
    return render(request, "app/alta_elementos.html", { 'elementos': elementos })

def alta_participantes(request):
    participantes = ParticipantesForm(request.POST or None, request.FILES or None)
    if participantes.is_valid():
        participantes.save()
        return redirect(consulta_participantes)
    return render(request, "app/alta_participantes.html", { 'participantes': participantes })
