from django.test import TestCase
from .models import Person
from person.serializers import PersonSerializer

class ModelTestCase(TestCase):
    def test_class_can_be_created(self):
        Person.objects.create()

class SerializerTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name='Harry', lastname='Potter', genre='M', alive='1', active='1')

    def serializer_can_convert_to_json(self):
        person = Person.objects.get(name='Harry')
        serializer = PersonSerializer(person)
        json_expected = {'name': 'arry', 'lastname': 'Potter', 'genre': 'M', 'alive': '1', 'active': '1'}
        self.assertEqual(serializer.data, json_expected)
