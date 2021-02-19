from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


def three(request):
    template = loader.get_template('three/animation.html')
    context = {}
    return HttpResponse(template.render(context, request))

def equations(request):
    template = loader.get_template('three/equations.html')
    context = {}
    return HttpResponse(template.render(context, request))

def experiment(request):
    template = loader.get_template('three/experiment.html')
    context = {}
    return HttpResponse(template.render(context, request))

def tankofnet(request):
    template = loader.get_template('three/tankofnet.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aromaticChart(request):
    template = loader.get_template('three/aromaticChart.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aliphaticChart(request):
    template = loader.get_template('three/aliphaticChart.html')
    context = {}
    return HttpResponse(template.render(context, request))

def tank(request):
    template = loader.get_template('three/tank.html')
    context = {}
    return HttpResponse(template.render(context, request))

def guiexample(request):
    template = loader.get_template('three/guiexample.html')
    context = {}
    return HttpResponse(template.render(context, request))

def periodic(request):
    template = loader.get_template('three/periodic.html')
    context = {}
    return HttpResponse(template.render(context, request))

def base(request):
    template = loader.get_template('three/base.html')
    context = {}
    return HttpResponse(template.render(context, request))

def alcohol(request):
    template = loader.get_template('three/alcohol.html')
    context = {}
    return HttpResponse(template.render(context, request))

def molecules(request):
    template = loader.get_template('three/molecules.html')
    context = {}
    return HttpResponse(template.render(context, request))

def desmos(request):
    template = loader.get_template('three/desmos.html')
    context = {}
    return HttpResponse(template.render(context, request))
