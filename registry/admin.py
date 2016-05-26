from django.contrib import admin

from models import *


class CheckedDataAdmin(admin.ModelAdmin):
    list_display = (
        'entryid',
        'passid',
        'reqid',
        'isvalid'
    )
    search_fields = (
        'passid__firstname',
        'passid__lastname',
        'passid__series',
        'passid__number',

        'reqid__date',
        'reqid__firstname',
        'reqid__lastname',
        'reqid__purpose',
        'reqid__applicantinfo',

        'isvalid',
    )


class RPassportAdmin(admin.ModelAdmin):
    list_display = (
        'passportid',
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
        'birthdate'
    )

class InPassportAdmin(admin.ModelAdmin):
    list_display = (
        'passportid',
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
        'birthdate'
    )


class ExtractAdmin(admin.ModelAdmin):
    list_display = (
        'extractid',
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
        'personid',
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
        'referenceid',
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
        'idreference',
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
        'requestid',
        'date',
        'firstname',
        'lastname',
        'purpose',
        'applicantinfo',
    )
    search_fields = (
        'date',
        'firstname',
        'lastname',
        'purpose',
        'applicantinfo',
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Inpassport, InPassportAdmin)
admin.site.register(Registeredpassport, RPassportAdmin)
admin.site.register(Extract, ExtractAdmin)
admin.site.register(Checkedindata, CheckedDataAdmin)
admin.site.register(Negativereference, NReferenceAdmin)
admin.site.register(Positivereference, PReferenceAdmin)
admin.site.register(Request, RequestAdmin)
