from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


def edumap(request):
    template = loader.get_template('edumap/edumap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def firstMap(request):
    template = loader.get_template('edumap/firstMap.html')
    context = {}
    return HttpResponse(template.render(context, request))

def bangladesh(request):
    template = loader.get_template('edumap/bangladesh.html')
    context = {}
    return HttpResponse(template.render(context, request))
