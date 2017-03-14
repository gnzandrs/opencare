from django.db import models

class Treatment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    description = models.CharField(max_length=45, blank=False, null=False)
    date_begin = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    date_end = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    active = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'treatment'
