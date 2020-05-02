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

def hydrogen(request):
    template = loader.get_template('three/hydrogen.html')
    context = {}
    return HttpResponse(template.render(context, request))

def experiment(request):
    template = loader.get_template('three/experiment.html')
    context = {}
    return HttpResponse(template.render(context, request))
