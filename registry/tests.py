#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from models import Person
from models import Inpassport
from models import Registeredpassport
from models import Positivereference
from models import Negativereference
from models import Extract
from models import Request
from models import Checkedindata


# class RegisteredpassportMethodTests(TestCase):
#     def setUp(self):
#         Registeredpassport.objects.create(
#             passportid='1',
#             series='CB',
#             number='232344',
#         )
#
#     def testRPassportAdd(self):
#         p = Registeredpassport.objects.get(passportid=1)
#         self.assertIsInstance(p, Registeredpassport)
#

class PersonMethodTests(TestCase):
    def setUp(self):
        Registeredpassport.objects.create(
                        passportid='1',
                        series='CB',
                        number='232344',
                    )
        r = Registeredpassport.objects.get(passportid=1)
        Person.objects.create(personid='1',
                              workplace='Test workplace',
                              workpost='Director',
                              checkresult='Check',
                              startingterm='2012-12-10',
                              passportid= r,
                              taxcode='344562225601'
                              )

    def testPersonAdd(self):
        p = Person.objects.get(personid=1)
        self.assertIsInstance(p, Person)


# class RequestMethodTests(TestCase):
#     def setUp(self):
#         Request.objects.create(
#             firstname="Дебил"
#         )
#
#     def testRequestAdd(self):
#         p = Request.objects.get(firstname="Дебил")
#         self.assertIsInstance(p, Request)

