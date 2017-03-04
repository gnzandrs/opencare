from django.test import TestCase
from .models import Person

class PersonTestCase(TestCase):
    def person_class_can_be_created():
        Person.objects.create()
