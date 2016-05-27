#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from models import *
import pdfkit


def registry(request):
    person = Person.objects.all()
    return render(request, "registry.html", {'person': person})


def search(request):
    if request.method == 'GET':
        return render(request, "search.html")
    else:
        s = request.POST.get("search")
        searching = s.split(' ')
        result = []
        for p in searching:
            passport = Registeredpassport.objects.all()
            person = Person.objects.all()
            filt = passport.filter(firstname__contains=p)
            if filt:
                for f in filt:
                    result.append(f.id)
            filt = passport.filter(secondname__contains=p)
            if filt:
                for f in filt:
                    result.append(f.id)
            filt = passport.filter(lastname__contains=p)
            if filt:
                for f in filt:
                    result.append(f.id)
            filt = person.filter(workplace__contains=p)
            if filt:
                for f in filt:
                    result.append(f.id)
            filt = person.filter(workpost__contains=p)
            if filt:
                for f in filt:
                    result.append(f.id)
        person = []
        result = list(set(result))
        for res in result:
            person.append(Person.objects.get(passportid=res))
        return render(request, "results.html", {'person': person})


def requests(request):
    if request.method == 'GET':
        return render(request, "request.html")
    else:
        s = request.POST.get("search")
        try:
            req = Request.objects.get(id=s)
        except Request.DoesNotExist:
            return render(request, "request.html", {'error_msg' : "Такого запиту не існує"})
        except:
            return render(request, "request.html", {'error_msg' : "Будь ласка, введіть коректні дані."})
        if req.answertype == 0:
            extracts = Extract.objects.all()
            for e in extracts:
                if e.requestid == req.id:
                    return redirect('request_result', e, 0)
            else:
                return redirect('request_result', None)
        else:
            pos_ref = Positivereference.objects.all()
            for p in pos_ref:
                if p.requestid == req.id:
                    return redirect('request_result', p, 1)
            else:
                neg_ref = Negativereference.objects.all()
                for n in neg_ref:
                    if n.requestid == req.id:
                        return redirect('request_result', n, 0)
                else:
                    return redirect('request_result', None, 0)


def request_result(request, data, type):
    if data is not None:
        if data.answertype == 0:
            extract = get_object_or_404(Extract, pk=data.id)
            if 'to_pdf_btn' in request.GET:
                context = {'e': extract, 'export_mode': True}
                return render_to_pdf('negative_extract.html', context)
            else:
                context = {'e' : extract, 'export_mode': False}
                return render(request, 'request_results.html', context)
        if data.answertype == 1:
            if 'to_pdf_btn' in request.GET:
                if type == 1:
                    pos_ref = get_object_or_404(Positivereference, pk=data.id)
                    context = {'e': pos_ref, 'export_mode': True}
                    return render_to_pdf('pos_ref.html', context)
                else:
                    neg_ref = get_object_or_404(Negativereference, pk=data.id)
                    context = {'e': neg_ref, 'export_mode': True}
                    return render_to_pdf('neg_ref.html', context)
            else:
                if type == 1:
                    pos_ref = get_object_or_404(Positivereference, pk=data.id)
                    context = {'e': pos_ref, 'export_mode': False}
                    return render(request, 'request_results.html', context)
                else:
                    neg_ref = get_object_or_404(Negativereference, pk=data.id)
                    context = {'e': neg_ref, 'export_mode': True}
                    return render(request, 'request_results.html', context)


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8"
        }

    pdf = pdfkit.from_string(html, False, options=options)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    return response
