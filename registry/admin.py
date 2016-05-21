from django.contrib import admin

from models import *


class RPassportAdmin(admin.ModelAdmin):
    list_display = ('passportid', 'firstname', 'lastname')


class InPassportAdmin(admin.ModelAdmin):
    list_display = ('passportid', 'firstname', 'lastname')


class ExtractAdmin(admin.ModelAdmin):
    list_display = ('extractid', 'personid', 'lastname')

class RPassportAdmin(admin.ModelAdmin):
    list_display = ('passportid', 'firstname', 'lastname')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('personid', 'passportid', 'workplace')


admin.site.register(Person, PersonAdmin)
admin.site.register(Inpassport, InPassportAdmin)
admin.site.register(Registeredpassport, RPassportAdmin)
admin.site.register(Extract)
admin.site.register(Checkedindata)
admin.site.register(Negativereference)
admin.site.register(Positivereference)
admin.site.register(Request)
