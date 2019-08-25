from decimal import Decimal

from django.db import models


class BlastQuery(models.Model):
    query_id = models.CharField(max_length=200)
    # query_sequence = models.TextField()
    pub_date = models.DateTimeField('updated')

    def __str__(self):
        return self.query_id


class BlastResult(models.Model):
    query = models.ForeignKey(BlastQuery,
                              related_name='results',
                              on_delete=models.CASCADE)
    subject_id = models.CharField(max_length=200)
    qstart = models.IntegerField()
    qend = models.IntegerField()
    sstart = models.IntegerField()
    send = models.IntegerField()
    pident = models.DecimalField(default=Decimal('0.00'), max_digits=5,
                                 decimal_places=2)
    length = models.IntegerField()
    mismatch = models.IntegerField()
    gapopen = models.DecimalField(default=Decimal('0.00'), max_digits=5,
                                  decimal_places=2)
    evalue = models.DecimalField(default=Decimal('0.00'), max_digits=10,
                                 decimal_places=10)
    bitscore = models.DecimalField(default=Decimal('0.00'), max_digits=20,
                                   decimal_places=2)

    def __str__(self):
        return "id: {}, start: {}, end: {}, pident: {}".format(self.subject_id,
                                                               self.sstart,
                                                               self.send,
                                                               self.pident)
