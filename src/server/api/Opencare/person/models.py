from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    lastname = models.CharField(max_length=45, blank=False, null=False)
    genre = models.CharField(max_length=1, blank=True, null=True)
    alive = models.IntegerField(blank=False, null=False)
    active = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'person'
