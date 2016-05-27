from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


@python_2_unicode_compatible
class Extract(models.Model):
    number = models.IntegerField(unique=True)
    formingdate = models.DateField(blank=True, null=True)
    applicantinfo = models.CharField(max_length=255, blank=True, null=True)
    requestid = models.ForeignKey('Request', on_delete=models.CASCADE)
    personid = models.ForeignKey('Person', on_delete=models.CASCADE)
    personwhomadeextract = models.CharField(max_length=255, blank=True, null=True)
    personwhosignsextract = models.CharField(max_length=255, blank=True, null=True)
    personswhosignsextractpost = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.personid.passportid.firstname + ' ' + self.personid.passportid.lastname)


@python_2_unicode_compatible
class Inpassport(models.Model):
    series = models.CharField(max_length=2)
    number = models.IntegerField()
    firstname = models.CharField(max_length=45, blank=True, null=True)
    secondname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=45, blank=True, null=True)
    givendate = models.DateField(blank=True, null=True)
    givenby = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


@python_2_unicode_compatible
class Negativereference(models.Model):
    requestid = models.ForeignKey('Request', on_delete=models.CASCADE)
    personwhomadereference = models.CharField(max_length=255, blank=True, null=True)
    personwhosignsreference = models.CharField(max_length=255, blank=True, null=True)
    personswhosignsreferencepost = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.requestid.firstname\
            + ' ' + self.requestid.lastname + ' negative')


@python_2_unicode_compatible
class Person(models.Model):
    workplace = models.CharField(max_length=255)
    workpost = models.CharField(max_length=255)
    checkresult = models.CharField(max_length=255)
    startingterm = models.DateField(blank=True, null=True)
    passportid = models.ForeignKey('Registeredpassport', on_delete=models.CASCADE)
    taxcode = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.passportid.firstname + ' ' + self.passportid.lastname + ' ' + self.workplace + ' ' + self.workpost


@python_2_unicode_compatible
class Positivereference(models.Model):
    requestid = models.ForeignKey('Request', on_delete=models.CASCADE)
    personid = models.ForeignKey('Person', on_delete=models.CASCADE)
    personwhomadereference = models.CharField(max_length=255, blank=True, null=True)
    personwhosignsreference = models.CharField(max_length=255, blank=True, null=True)
    personswhosignsreferencepost = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.requestid.firstname \
               + ' ' + self.requestid.lastname + ' positive')


@python_2_unicode_compatible
class Registeredpassport(models.Model):
    series = models.CharField(max_length=2)
    number = models.IntegerField(unique=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    secondname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=45, blank=True, null=True)
    givendate = models.DateField(blank=True, null=True)
    givenby = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


@python_2_unicode_compatible
class Request(models.Model):
    answertype = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    passportid = models.ForeignKey('Inpassport', on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    obtainway = models.IntegerField(blank=True, null=True)
    applicantinfo = models.CharField(max_length=255, blank=True, null=True)
    servicenotes = models.TextField(blank=True, null=True)
    taxcode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.purpose.encode('utf-8') + ' ' + self.firstname.encode('utf-8') + ' ' + self.lastname.encode(
            'utf-8'))
