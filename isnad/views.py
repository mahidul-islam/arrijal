from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect
import json

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

def graph3(request):
    template = loader.get_template('isnad/graph3.html')
    context = {}
    return HttpResponse(template.render(context, request))



def load(request):
    limit=300
    wdata = {}
    wdata['nodes'] = []
    wdata['links'] = []
    with open('isnad/static/isnad/datasets/all_rawis_smt.json') as json_file:
        ldata = json.load(json_file)
    with open('isnad/static/isnad/datasets/all_rawis.json') as json_file:
        aldata = json.load(json_file)
    for a in aldata['info']:
        if a['scholar_indx'] < limit:
            wdata['nodes'].append({
                'id': a['scholar_indx'],
                'name':a['name'],
                'grade':a['grade']
            })
    for l in ldata['links']:
        for t in l['target']:
            if not (str(t)) == "NA":
                if t < limit and l['source'] < limit :
                    wdata['links'].append({
                        'source': l['source'],
                        'target': t
                    })
    with open('isnad/static/isnad/datasets/some_rawis.json', 'w') as outfile:
        json.dump(wdata, outfile)
    return redirect('isnad:isnad')
