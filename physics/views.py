from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


def physics(request):
    template = loader.get_template('physics/physics.html')
    context = {}
    return HttpResponse(template.render(context, request))

def firstGame(request):
    template = loader.get_template('physics/firstGame.html')
    context = {}
    return HttpResponse(template.render(context, request))

def mod2d(request):
    template = loader.get_template('physics/mod2d.html')
    context = {}
    return HttpResponse(template.render(context, request))

def threed(request):
    template = loader.get_template('physics/threed.html')
    context = {}
    return HttpResponse(template.render(context, request))

def threed_mobile(request):
    template = loader.get_template('physics/threed_mobile.html')
    context = {}
    return HttpResponse(template.render(context, request))
