from django.db import models

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'

class Medicine:
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine'

class Person:
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    lastname = models.CharField(max_length=45, blank=False, null=False)
    genre = models.CharField(max_length=1, blank=True, null=True)
    alive = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'person'

class Relationship:
    id = models.IntegerField(primary_key=True)
    relationship_type = models.CharField(max_length=45, blank=False, null=False)
    blood = models.BooleanField()
    person_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relationship'

class Role:
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    description = models.CharField(max_length=100, blank=True, null=True)
    field = models.CharField(max_length=45, blank=False, null=False)
    active = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'role'

class Treatment:
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    date_begin = models.DateTimeField(blank=False, null=False)
    date_end = models.DateTimeField(blank=False, null=False)
    active = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'treatment'
