from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


def map(request):
    template = loader.get_template('map/map.html')
    context = {}
    return HttpResponse(template.render(context, request))

def firstMap(request):
    template = loader.get_template('map/firstMap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def bangladesh(request):
    template = loader.get_template('map/bangladesh.html')
    context = {}
    return HttpResponse(template.render(context, request))

def bdgeojson(request):
    template = loader.get_template('map/bdgeojson.html')
    context = {}
    return HttpResponse(template.render(context, request))

def d3(request):
    template = loader.get_template('map/d3.html')
    context = {}
    return HttpResponse(template.render(context, request))

def povertymap(request):
    template = loader.get_template('map/povertymap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def markermap(request):
    template = loader.get_template('map/markermap.html')
    context = {}
    return HttpResponse(template.render(context, request))
