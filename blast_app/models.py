from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class BlastResult(models.Model):
    query_id = models.CharField(max_length=200)
    subject_id = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.query_id
