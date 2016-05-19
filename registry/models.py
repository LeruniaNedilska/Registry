# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Checkedindata(models.Model):
    entryid = models.AutoField(db_column='entryId', unique=True, primary_key=True)  # Field name made lowercase.
    passid = models.ForeignKey('Inpassport', models.DO_NOTHING, db_column='passId')  # Field name made lowercase.
    reqid = models.ForeignKey('Request', models.DO_NOTHING, db_column='reqId')  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'checkedindata'
        unique_together = (('entryid', 'passid', 'reqid'),)


class Extract(models.Model):
    extractid = models.AutoField(db_column='extractId', unique=True, primary_key=True)  # Field name made lowercase.
    number = models.IntegerField(unique=True)
    formingdate = models.DateField(db_column='formingDate', blank=True, null=True)  # Field name made lowercase.
    applicantinfo = models.CharField(db_column='ApplicantInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extractscol = models.CharField(db_column='Extractscol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='requestId')  # Field name made lowercase.
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='personId')
    personwhomadeextract = models.CharField(db_column='PersonWhoMadeExtract', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personwhosignsextract = models.CharField(db_column='PersonWhoSignsExtract', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personswhosignsextractpost = models.CharField(db_column='PersonsWhoSignsExtractPost', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extract'
        unique_together = (('extractid', 'requestid'),)


class Inpassport(models.Model):
    passportid = models.AutoField(db_column='passportId', primary_key=True)  # Field name made lowercase.
    series = models.CharField(max_length=2)
    number = models.IntegerField()
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    secondname = models.CharField(db_column='secondName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='birthPlace', max_length=45, blank=True, null=True)  # Field name made lowercase.
    givendate = models.DateField(db_column='givenDate', blank=True, null=True)  # Field name made lowercase.
    givenby = models.CharField(db_column='givenBy', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inpassport'


class Negativereference(models.Model):
    referenceid = models.AutoField(db_column='referenceId', unique=True, primary_key=True)  # Field name made lowercase.
    requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='requestId')  # Field name made lowercase.
    personwhomadereference = models.CharField(db_column='PersonWhoMadeReference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personwhosignsreference = models.CharField(db_column='PersonWhoSignsReference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personswhosignsreferencepost = models.CharField(db_column='PersonsWhoSignsReferencePost', max_length=255, blank=True, null=True)  # Field name made lowercase.
    negativereferencecol = models.CharField(db_column='NegativeReferencecol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'negativereference'
        unique_together = (('referenceid', 'requestid'),)


class Person(models.Model):
    personid = models.AutoField(db_column='personId', unique=True, primary_key=True)  # Field name made lowercase.
    workplace = models.CharField(db_column='workPlace', max_length=255)  # Field name made lowercase.
    workpost = models.CharField(db_column='workPost', max_length=255)  # Field name made lowercase.
    checkresult = models.CharField(db_column='checkResult', max_length=255)  # Field name made lowercase.
    startingterm = models.DateField(db_column='StartingTerm')  # Field name made lowercase.
    passportid = models.ForeignKey('Registeredpassport', models.DO_NOTHING, db_column='passportID')
    taxcode = models.IntegerField(db_column='TaxCode', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.passportid.firstname + ' ' + self.passportid.lastname + ' ' + self.workplace + ' ' + self.workpost

    class Meta:
        managed = False
        db_table = 'person'
        unique_together = (('personid', 'passportid'),)


class Positivereference(models.Model):
    idreference = models.AutoField(db_column='idReference', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='personId')  # Field name made lowercase.
    personwhomadereference = models.CharField(db_column='PersonWhoMadeReference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personwhosignsreference = models.CharField(db_column='PersonWhoSignsReference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personswhosignsreferencepost = models.CharField(db_column='PersonsWhoSignsReferencePost', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'positivereference'


class Registeredpassport(models.Model):
    passportid = models.AutoField(db_column='passportId', primary_key=True)  # Field name made lowercase.
    series = models.CharField(max_length=2)
    number = models.IntegerField(unique=True)
    firstname = models.CharField(db_column='firstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    secondname = models.CharField(db_column='secondName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='birthPlace', max_length=45, blank=True, null=True)  # Field name made lowercase.
    givendate = models.DateField(db_column='givenDate', blank=True, null=True)  # Field name made lowercase.
    givenby = models.CharField(db_column='givenBy', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registeredpassport'


class Request(models.Model):
    requestid = models.AutoField(db_column='requestId', primary_key=True)  # Field name made lowercase.
    answertype = models.IntegerField(db_column='answerType', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secondname = models.CharField(db_column='secondName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(max_length=255, blank=True, null=True)
    obtainway = models.IntegerField(db_column='obtainWay', blank=True, null=True)  # Field name made lowercase.
    applicantinfo = models.CharField(db_column='ApplicantInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    servicenotes = models.TextField(db_column='serviceNotes', blank=True, null=True)  # Field name made lowercase.
    taxcode = models.IntegerField(db_column='TaxCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'request'
