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
    # query_sequence = models.TextField()
    subject_id = models.CharField(max_length=200)
    sstart = models.IntegerField()
    send = models.IntegerField()
    # alignment_sequence = models.TextField()

    def __str__(self):
        return "id: {}, start: {}, end: {}".format(self.subject_id,
                                                   self.sstart,
                                                   self.send)
