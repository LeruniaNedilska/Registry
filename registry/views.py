#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from models import *
import pdfkit
from wkhtmltopdf.views import PDFTemplateResponse


def registry(request):
    person = Person.objects.all()
    return render(request, "registry.html", {'person': person})


def base(request):
    return HttpResponseRedirect("/main")


def test(request):
    return render(request, "positive_reference.html")


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
    if request.method=='POST':
        s = request.POST.get("search")
        try:
            req = Request.objects.get(id=s)
        except Request.DoesNotExist:
            return render(request, "request.html", {'error_msg': "Такого запиту не існує"})
        except:
            return render(request, "request.html", {'error_msg': "Будь ласка, введіть коректні дані."})
        if req.answertype == 0:
            pos_extracts = PositiveExtract.objects.all()
            for e in pos_extracts:
                if e.requestid == req:
                    if request.GET.get("down"):
                        context = {'e': e, 'export_mode': True, 'isValid': True}
                        return render_to_pdf(request, 'positive_reference.html', context),
                    return request_result(request, req, 1)
            else:
                neg_extracts = NegativeExtract.objects.all()
                for e in neg_extracts:
                    if e.requestid == req.id:
                        return request_result(request, req, 0)
                else:
                    return request_result(request, None, 0)
        else:
            pos_ref = Positivereference.objects.all()
            for p in pos_ref:
                if p.requestid == req.id:
                    return redirect(request_result, p, 1)
            else:
                neg_ref = Negativereference.objects.all()
                for n in neg_ref:
                    if n.requestid == req.id:
                        return redirect('request_result', n, 0)
                else:
                    return redirect('request_result', None, 0)
    else:
        return render(request, 'request.html')


def request_result(request, data, type):
    if data is not None:
       if data.answertype == 0:
              if type == 1:
                    pos_ext = get_object_or_404(PositiveExtract, pk=data.id)
                    person = get_object_or_404(Person, pk=data.id)
                    context = {'e': pos_ext, 'export_mode': True, 'isValid': True}
                    return render_to_pdf(request, 'positive_extract.html', context)
              else:
                    neg_ext = get_object_or_404(NegativeExtract, pk=data.id)
                    context = {'e': neg_ext, 'export_mode': True, 'isValid': True}
                    return render_to_pdf('negative_extract.html', context)
       else:
                if type == 1:
                    pos_ref = get_object_or_404(Positivereference, pk=data.id)
                    context = {'e': pos_ref, 'export_mode': True, 'isValid': True}
                    return render_to_pdf('positive_reference.html', context)
                else:
                    neg_ref = get_object_or_404(Negativereference, pk=data.id)
                    context = {'e': neg_ref, 'export_mode': True, 'isValid': True}
                    return render_to_pdf('negative_reference.html', context)
    else:
        context = {'isValid': False}
        return render(request, 'request_results.html', context)


def render_to_pdf(request, template_src, context_dict):
    return render(request, template_src, context=context_dict)
