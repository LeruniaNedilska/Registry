from django.contrib import admin

from models import *

# encoding=utf8
from django.contrib import admin

from models import *

from datetime import date

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def generate_response(modeladmin, request, request_set):
    reg_passports = Registeredpassport.objects.all()

    for request in request_set:
        req_passport_identifier = {request.passportid.series: request.passportid.number}
        reg_passport_identifiers = []
        for passport in reg_passports:
            reg_passport_identifiers.append({passport.series: passport.number})

        pos_extracts = PositiveExtract.objects.all()
        neg_extracts = NegativeExtract.objects.all()

        pos_extract = []
        neg_extract = []

        if request.answertype == 0:
            try:
                pos_extract = PositiveExtract.objects.get(requestid=request)
            except PositiveExtract.DoesNotExist:
                try:
                    neg_extract = NegativeExtract.objects.get(requestid=request)
                except NegativeExtract.DoesNotExist:
                    if req_passport_identifier in reg_passport_identifiers:
                        add_positive_response(request, reg_passports.get(series=request.passportid.series,
                                                                         number=request.passportid.number))
                    else:
                        add_negative_response(request)
        else:
            try:
                pos_ref = Positivereference.objects.get(requestid=request)
            except Positivereference.DoesNotExist:
                try:
                    neg_ref = Negativereference.objects.get(requestid=request)
                except Negativereference.DoesNotExist:
                    if req_passport_identifier in reg_passport_identifiers:
                        add_positive_response(request, reg_passports.get(series=request.passportid.series,
                                                                         number=request.passportid.number))
                    else:
                        add_negative_response(request)
generate_response.short_description = "Generate response"


def add_positive_response(request, passport):
    if request.answertype == 0:
        PositiveExtract.objects.create(
            number=request.pk,
            formingdate=date.today(),
            applicantinfo=request.applicantinfo,
            requestid=request,
            personid=passport.person_set.get()
        )
    else:
        Positivereference.objects.create(
            requestid=request,
            personid=passport.person_set.get()
        )


def add_negative_response(request):
        if request.answertype == 0:
            NegativeExtract.objects.create(
                number=request.pk,
                formingdate=date.today(),
                applicantinfo=request.applicantinfo,
                requestid=request,
            )
        else:
            Negativereference.objects.create(
                requestid=request
            )


class RPassportAdmin(admin.ModelAdmin):
    list_display = (
        'series',
        'number',
        'firstname',
        'lastname',
        'birthdate',
    )
    search_fields = (
        'series',
        'number',
        'firstname',
        'lastname',
        'birthdate',
    )


class InPassportAdmin(admin.ModelAdmin):
    list_display = (
        'series',
        'number',
        'firstname',
        'lastname',
        'birthdate',
    )
    search_fields = (
        'series',
        'number',
        'firstname',
        'lastname',
        'birthdate',
    )


class PositiveExtractAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'formingdate',
        'personid',
        'requestid'
    )
    search_fields = (
        'number',
        'formingdate',

        'personid__passportid__firstname',
        'personid__passportid__lastname',
        'personid__passportid__series',
        'personid__passportid__number',
        'personid__workplace',
        'personid__workpost',
        'personid__checkresult',
        'personid__taxcode',

        'requestid__date',
        'requestid__firstname',
        'requestid__lastname',
        'requestid__purpose',
        'requestid__applicantinfo',
    )


class NegativeExtractAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'formingdate',
        'requestid'
    )
    search_fields = (
        'number',
        'formingdate',

        'requestid__date',
        'requestid__firstname',
        'requestid__lastname',
        'requestid__purpose',
        'requestid__applicantinfo',
    )


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'passportid',
        'workplace',
        'workpost',
        'startingterm',
        'checkresult',
        'taxcode',
    )
    search_fields = (
        'passportid__firstname',
        'passportid__lastname',
        'passportid__series',
        'passportid__number',
        'workplace',
        'workpost',
        'checkresult',
        'taxcode',
    )
    list_filter = [
        'passportid__firstname',
        'passportid__lastname',
        'startingterm',
    ]


class NReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'requestid',
    )
    search_fields = (
        'requestid__date',
        'requestid__firstname',
        'requestid__lastname',
        'requestid__purpose',
        'requestid__applicantinfo',
    )


class PReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'requestid',
        'personid',
    )
    search_fields = (
        'requestid__date',
        'requestid__firstname',
        'requestid__lastname',
        'requestid__purpose',
        'requestid__applicantinfo',

        'personid__passportid__firstname',
        'personid__passportid__lastname',
        'personid__passportid__series',
        'personid__passportid__number',
        'personid__workplace',
        'personid__workpost',
        'personid__checkresult',
        'personid__taxcode',
    )


class RequestAdmin(admin.ModelAdmin):
    actions = [generate_response]
    list_display = (
        'id',
        'date',
        'passportid',
        'purpose',
        'applicantinfo',
    )
    search_fields = (
        'date',
        'passportid__firstname',
        'passportid__lastname',
        'passportid__series',
        'passportid__number',
        'purpose',
        'applicantinfo',
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Inpassport, InPassportAdmin)
admin.site.register(Registeredpassport, RPassportAdmin)
admin.site.register(PositiveExtract, PositiveExtractAdmin)
admin.site.register(NegativeExtract, NegativeExtractAdmin)
admin.site.register(Negativereference, NReferenceAdmin)
admin.site.register(Positivereference, PReferenceAdmin)
admin.site.register(Request, RequestAdmin)
