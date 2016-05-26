#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from models import *


class CheckedindataMethodTests(TestCase):
    def setUp(self):
        Checkedindata.objects.create(
            passid=Inpassport.objects.create(
                series='VF',
                number='344551',
                firstname='Jane',
                secondname='Maria',
                lastname='Doe',
                birthdate='1999-12-12',
                birthplace='London',
                givendate='2015-12-30',
                givenby='London CV'
            ),
            reqid=Request.objects.create(
                answertype='1',
                date='2016-05-12',
                firstname='Jane',
                secondname='Maria',
                lastname='Doe',
                purpose='Work check',
                obtainway='1',
                applicantinfo='Nice person',
                servicenotes='notes',
                taxcode='123424'
            ),
            isvalid='1'
        )

    def test_add(self):
        data = Checkedindata.objects.get(id=1)
        self.assertIsInstance(data, Checkedindata)

    def test_delete(self):
        data = Checkedindata.objects.get(id='1')
        data.delete()
        try:
            obj = Checkedindata.objects.get(id=1)
        except Checkedindata.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        id = 1
        data = Checkedindata.objects.get(pk=id)
        data.passid.firstname = 'Name'
        data.save()
        updated_data = Checkedindata.objects.get(name='Name')
        self.assertEqual(updated_data.id, id)


class InpassportMethodTests(TestCase):
    def setUp(self):
        Inpassport.objects.create(
            series='DB',
            number='1234323',
            firstname='Dema'
        )

    def test_add(self):
        p = Inpassport.objects.get(firstname='Dema')
        self.assertIsInstance(p, Inpassport)

