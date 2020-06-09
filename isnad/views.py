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

def sgraph(request):
    template = loader.get_template('isnad/sgraph.html')
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

def graph4(request):
    template = loader.get_template('isnad/graph4.html')
    context = {}
    return HttpResponse(template.render(context, request))

def graph5(request):
    template = loader.get_template('isnad/graph5.html')
    context = {}
    return HttpResponse(template.render(context, request))


def sload(request):
    start=0;
    end=40023;
    wdata = {}
    wdata['nodes'] = []
    wdata['links'] = []
    with open('isnad/static/isnad/datasets/all_rawis_smt.json') as json_file:
        ldata = json.load(json_file)
    with open('isnad/static/isnad/datasets/all_rawis.json') as json_file:
        aldata = json.load(json_file)
    for a in aldata['info']:
        if start <= a['scholar_indx'] <= end:
            wdata['nodes'].append({
                'id': a['scholar_indx'],
                'name':a['name'],
                'group':a['grade']
            })
    for index,l in enumerate(ldata['links']):
        for t in l['target']:
            if not (str(t)) == "NA":
                if start <= t <= end and start <= l['source'] <= end:
                    wdata['links'].append({
                        'source': l['source'],
                        'target': t,
                    })
    with open('isnad/static/isnad/datasets/some_rawis.json', 'w') as outfile:
        json.dump(wdata, outfile)
    return redirect('isnad:isnad')


def iload(request):
    name=""
    start=0
    end=34442
    j=0
    all="hadiths"
    source=""
    chapter=""
    rawis=[]
    dic={}
    wdata = {}
    wdata['nodes'] = []
    wdata['links'] = []

    with open('isnad/static/isnad/datasets/all_hadiths_clean.json') as json_file:
        aldata = json.load(json_file)
    with open('isnad/static/isnad/datasets/all_hadiths_chain.json') as json_file:
        cdata = json.load(json_file)
    with open('isnad/static/isnad/datasets/all_rawis.json') as json_file:
        rdata = json.load(json_file)
    with open('isnad/static/isnad/datasets/getrawisindex.json') as json_file:
        getindex = json.load(json_file)

    wdata['nodes'].append({
        'id': all,
        'group':all,
        'level':1,
        'book':'all'
    })

    for index,a in enumerate(aldata['info']):
        if start <= index <= end:
            wdata['nodes'].append({
                'id': index,
                'name': a['hadith_no'],
                'group':"hadith",
                'level':4,
                'text':a['text_en'],
                'hadith_no':a['hadith_no'].strip(),
                'book':a['source'].strip()
            })
            if a['hadith_no'] == " 1 ":
                source = aldata['info'][index]['source']
                wdata['nodes'].append({
                    'id': a['source'],
                    'name':a['source'],
                    'group': "source",
                    'level':2,
                    'book':a['source'].strip()
                })
                wdata['links'].append({
                    'source': all ,
                    'target': a['source'],
                    'book':a['source'].strip()

                })
            if a['id'] == 0:
                chapter = aldata['info'][index]['chapter']
                print(chapter)
                wdata['nodes'].append({
                    'id': a['chapter'],
                    'name':a['chapter'],
                    'group':"chapter",
                    'level':3,
                    'chapter':a['chapter'],
                    'book':a['source'].strip()
                })
            wdata['links'].append({
                'source': source ,
                'target': chapter,
                'chapter':a['chapter'],
                'book':a['source'].strip()

            })
            wdata['links'].append({
                'source': chapter ,
                'target': index,
                'hadith_no':a['hadith_no'].strip(),
                'book':a['source'].strip(),
                'level':4
            })

    for index,c in enumerate(cdata['info']):
        j=0
        if  start <= index <= end:
            hadith_id = index
            for s in c['chain_indx']:
                if str(c['chain_indx'][j]) not in rawis:
                    rawis.append(str(cdata['info'][index]['chain_indx'][j]))
                    name=str(c['chain_indx'][j])
                    if str(cdata['info'][index]['chain_indx'][j]) in getindex:
                        name = rdata['info'][getindex[str(cdata['info'][index]['chain_indx'][j])]]['name']
                    wdata['nodes'].append({
                        'id': str(c['chain_indx'][j]),
                        'name':name,
                        'group':"rawis",
                        'level':5,
                        'list':list(aldata['info'][index]['hadith_no'].strip().split(" "))
                    })
                    #dic.add(len(rawis)-1, len(wdata['nodes'])-1)
                    dic[len(rawis)-1]=len(wdata['nodes'])-1
                else:
                    p=rawis.index(str(c['chain_indx'][j]))
                    k=dic[p]
                    wdata['nodes'][k]['list'].append(aldata['info'][index]['hadith_no'].strip())


                wdata['links'].append({
                    'source': hadith_id,
                    'target': str(c['chain_indx'][j]),
                    'hadith_no':aldata['info'][index]['hadith_no'].strip(),
                    'book':aldata['info'][index]['source'].strip()

                })
                if str(cdata['info'][index]['chain_indx'][j]) in getindex:
                    hadith_id = str(c['chain_indx'][j])
                j+=1
                print(hadith_id)
    with open('isnad/static/isnad/datasets/some_hadiths.json', 'w') as outfile:
        json.dump(wdata, outfile)
    return redirect('isnad:isnad')


def getrawisload(request):
    ind=""
    wdata = {}
    with open('isnad/static/isnad/datasets/all_rawis.json') as json_file:
        rdata = json.load(json_file)
    for index,r in enumerate(rdata['info']):
         wdata[rdata['info'][index]['scholar_indx']]=index
    with open('isnad/static/isnad/datasets/getrawisindex.json', 'w') as outfile:
        json.dump(wdata, outfile)
    return redirect('isnad:isnad')



def load(request):
    wdata = {}
    wdata['info'] = []
    with open('all_hadiths_clean.json') as json_file:
        aldata = json.load(json_file)
    for a in aldata['info']:
        if (a['chain_indx']):
            wdata['nodes'].append({
                'hadith_id': a['hadith_id'],
                'chain_indx': a['chain_indx']
            })
        else:
            wdata['nodes'].append({
                'hadith_id': a['hadith_id'],
                'chain_indx':[]
            })

    with open('all_hadiths_chain.json', 'w') as outfile:
        json.dump(wdata, outfile)
    return redirect('isnad:isnad')
