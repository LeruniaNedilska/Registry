from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Checkedindata(models.Model):
    entryid = models.AutoField(db_column='entryId', unique=True, primary_key=True)
    passid = models.ForeignKey('Inpassport', models.DO_NOTHING, db_column='passId')
    reqid = models.ForeignKey('Request', models.DO_NOTHING, db_column='reqId')
    isvalid = models.IntegerField(db_column='isValid', blank=True, null=True)

    list_display = ('entryId', 'passId', 'Request', 'isValid')

    def __str__(self):
        return self.passid.firstname + ' '\
            + self.passid.lastname + ' : '\
            + self.reqid.firstname + ' '\
            + self.reqid.lastname

    class Meta:
        managed = False
        db_table = 'checkedindata'
        ordering = ('entryid',)
        unique_together = (('entryid', 'passid', 'reqid'),)


@python_2_unicode_compatible
class Extract(models.Model):
    extractid = models.AutoField(db_column='extractId', unique=True, primary_key=True)
    number = models.IntegerField(unique=True)
    formingdate = models.DateField(db_column='formingDate', blank=True, null=True)
    applicantinfo = models.CharField(db_column='ApplicantInfo', max_length=255, blank=True, null=True)
    extractscol = models.CharField(db_column='Extractscol', max_length=45, blank=True, null=True)
    requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='requestId')
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='personId')
    personwhomadeextract = models.CharField(db_column='PersonWhoMadeExtract', max_length=255, blank=True, null=True)
    personwhosignsextract = models.CharField(db_column='PersonWhoSignsExtract', max_length=255, blank=True, null=True)
    personswhosignsextractpost = models.CharField(db_column='PersonsWhoSignsExtractPost', max_length=255, blank=True,
                                                  null=True)

    def __str__(self):
        return str(self.extractid) + ' ' + self.personid.passportid.firstname\
            + ' ' + self.personid.passportid.lastname

    class Meta:
        managed = False
        db_table = 'extract'
        ordering = ('extractid',)
        unique_together = (('extractid', 'requestid'),)


@python_2_unicode_compatible
class Inpassport(models.Model):
    passportid = models.AutoField(db_column='passportId', primary_key=True)
    series = models.CharField(max_length=2)
    number = models.IntegerField()
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)
    secondname = models.CharField(db_column='secondName', max_length=45, blank=True, null=True)
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)
    birthdate = models.DateField(db_column='birthDate', blank=True, null=True)
    birthplace = models.CharField(db_column='birthPlace', max_length=45, blank=True, null=True)
    givendate = models.DateField(db_column='givenDate', blank=True, null=True)
    givenby = models.CharField(db_column='givenBy', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    class Meta:
        managed = False
        ordering = ('passportid',)
        db_table = 'inpassport'


@python_2_unicode_compatible
class Negativereference(models.Model):
    referenceid = models.AutoField(db_column='referenceId', unique=True, primary_key=True)
    requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='requestId')
    personwhomadereference = models.CharField(db_column='PersonWhoMadeReference', max_length=255, blank=True, null=True)
    personwhosignsreference = models.CharField(db_column='PersonWhoSignsReference', max_length=255, blank=True,
                                               null=True)
    personswhosignsreferencepost = models.CharField(db_column='PersonsWhoSignsReferencePost', max_length=255,
                                                    blank=True, null=True)
    negativereferencecol = models.CharField(db_column='NegativeReferencecol', max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.referenceid) + ' ' + self.requestid.firstname\
            + ' ' + self.requestid.lastname + ' negative'

    class Meta:
        managed = False
        db_table = 'negativereference'
        ordering = ('referenceid',)
        unique_together = (('referenceid', 'requestid'),)


@python_2_unicode_compatible
class Person(models.Model):
    personid = models.AutoField(db_column='personId', unique=True, primary_key=True)
    workplace = models.CharField(db_column='workPlace', max_length=255)
    workpost = models.CharField(db_column='workPost', max_length=255)
    checkresult = models.CharField(db_column='checkResult', max_length=255)
    startingterm = models.DateField(db_column='StartingTerm')
    passportid = models.ForeignKey('Registeredpassport', models.DO_NOTHING, db_column='passportID')
    taxcode = models.IntegerField(db_column='TaxCode', blank=True, null=True)


    def __str__(self):
        return self.passportid.firstname + ' ' + self.passportid.lastname + ' ' + self.workplace + ' ' + self.workpost

    class Meta:
        managed = False
        db_table = 'person'
        ordering = ('personid',)
        unique_together = (('personid', 'passportid'),)


@python_2_unicode_compatible
class Positivereference(models.Model):
    idreference = models.AutoField(db_column='idReference', primary_key=True)
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='personId')
    personwhomadereference = models.CharField(db_column='PersonWhoMadeReference', max_length=255, blank=True, null=True)
    personwhosignsreference = models.CharField(db_column='PersonWhoSignsReference', max_length=255, blank=True,
                                               null=True)
    personswhosignsreferencepost = models.CharField(db_column='PersonsWhoSignsReferencePost', max_length=255,
                                                    blank=True, null=True)

    def __str__(self):
        return str(self.referenceid) + ' ' + self.requestid.firstname \
               + ' ' + self.requestid.lastname + ' positive'


    class Meta:
        managed = False
        ordering = ('idreference',)
        db_table = 'positivereference'


@python_2_unicode_compatible
class Registeredpassport(models.Model):
    passportid = models.AutoField(db_column='passportId', primary_key=True)
    series = models.CharField(max_length=2)
    number = models.IntegerField(unique=True)
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)
    secondname = models.CharField(db_column='secondName', max_length=45, blank=True, null=True)
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)
    birthdate = models.DateField(db_column='birthDate', blank=True, null=True)
    birthplace = models.CharField(db_column='birthPlace', max_length=45, blank=True, null=True)
    givendate = models.DateField(db_column='givenDate', blank=True, null=True)
    givenby = models.CharField(db_column='givenBy', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    class Meta:
        managed = False
        ordering = ('passportid',)
        db_table = 'registeredpassport'


@python_2_unicode_compatible
class Request(models.Model):
    requestid = models.AutoField(db_column='requestId', primary_key=True)
    answertype = models.IntegerField(db_column='answerType', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)
    secondname = models.CharField(db_column='secondName', max_length=255, blank=True, null=True)
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    obtainway = models.IntegerField(db_column='obtainWay', blank=True, null=True)
    applicantinfo = models.CharField(db_column='ApplicantInfo', max_length=255, blank=True, null=True)
    servicenotes = models.TextField(db_column='serviceNotes', blank=True, null=True)
    taxcode = models.IntegerField(db_column='TaxCode', blank=True, null=True)

    def __str__(self):
        return str(self.requestid) + ' '\
            + self.purpose + ' ' \
            + self.firstname + ' ' \
            + self.lastname + ' '

    class Meta:
        managed = False
        ordering = ('requestid',)
        db_table = 'request'
