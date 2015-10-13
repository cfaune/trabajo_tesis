from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    latest_remedio_list = Remedio.objects.order_by('-pub_date')[:5]
    template = loader.get_template('remedios/index.html')
    context = RequestContext(request, {
        'latest_remedio_list': latest_remedio_list,
    })
    return HttpResponse(template.render(context))

def detail(request, remedio_id):
    return HttpResponse("You're looking at question %s." % remedio_id)

def results(request, remedio_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % remedio_id)

def vote(request, remedio_id):
    return HttpResponse("You're voting on question %s." % remedio_id)



# Create your views here.