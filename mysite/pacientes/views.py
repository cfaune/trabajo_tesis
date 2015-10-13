from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    lista_pacientes = Paciente.objects.all()[:5]
    template = loader.get_template('pacientes/index.html')
    context = RequestContext(request, {
        'lista_pacientes': lista_pacientes,
    })
    return HttpResponse(template.render(context))

def detail(request, paciente_numero_ficha):
    paciente = Paciente.objects.filter(numero_ficha=paciente_numero_ficha).first()
    template = loader.get_template('pacientes/detail.html')
    context = RequestContext(request, {
        'paciente': paciente,
    })
    return HttpResponse(template.render(context))

def results(request, paciente_numero_ficha):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % paciente_numero_ficha)

def vote(request, paciente_numero_ficha):
    return HttpResponse("You're voting on question %s." % paciente_numero_ficha)