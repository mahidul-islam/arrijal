from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

def isnad(request):
    template = loader.get_template('isnad/isnad.html')
    context = {}
    return HttpResponse(template.render(context, request))

def igraph(request):
    template = loader.get_template('isnad/igraph.html')
    context = {}
    return HttpResponse(template.render(context, request))

def graph1(request):
    template = loader.get_template('isnad/graph1.html')
    context = {}
    return HttpResponse(template.render(context, request))

def graph2(request):
    template = loader.get_template('isnad/graph2.html')
    context = {}
    return HttpResponse(template.render(context, request))
