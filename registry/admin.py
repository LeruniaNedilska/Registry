from django.contrib import admin

from models import *

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


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


class ExtractAdmin(admin.ModelAdmin):
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
    list_display = (
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
admin.site.register(Extract, ExtractAdmin)
admin.site.register(Negativereference, NReferenceAdmin)
admin.site.register(Positivereference, PReferenceAdmin)
admin.site.register(Request, RequestAdmin)
