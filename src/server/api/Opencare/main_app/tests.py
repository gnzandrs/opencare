from django.test import TestCase
from .models import Company, Medicine, Person, Relationship, Role, Treatment

class CompanyTestCase(TestCase):
    def company_class_can_be_created():
        Company.objects.create()

class MedicineTestCase(TestCase):
    def medicine_class_can_be_created():
        Medicine.objects.create()

class PersonTestCase(TestCase):
    def person_class_can_be_created():
        Person.objects.create()

class RelationshipTestCase(TestCase):
    def relationship_class_can_be_created():
        Relationship.objects.create()

class RoleTestCase(TestCase):
    def role_class_can_be_created():
        Role.objects.create()

class TreatmentTestCase(TestCase):
    def treatment_class_can_be_created():
        Treatment.objetcs.create()
