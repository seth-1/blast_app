from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline

from celery import shared_task

from django.utils import timezone

from .models import BlastQuery, BlastResult


@shared_task
def my_add_task(a, b):
    return a + b


@shared_task
def prepare_blast(query='blast_app/data/test_sequence.fasta',
                  db='blast_app/data/proteins.fasta', evalue=0.001):
    query_id = query.split("/")[-1][:-6]
    blast_query = BlastQuery(query_id=query_id,
                             pub_date=timezone.now())
    blast_query.save()
    # blast_cmd = NcbiblastxCommandline(query=query, db=db, evalue=evalue)
    blast_cmd = NcbiblastxCommandline(query=query,
                                      db=db,
                                      evalue=evalue,
                                      outfmt=5,
                                      out='blast_app/results.xml')
    blast_cmd()  # Running blast in subprocess
    with open("blast_app/results.xml") as xml_handle:
        blast_rec = NCBIXML.read(xml_handle)
        for alignment in blast_rec.alignments:
            for hsp in alignment.hsps:
                b = BlastResult(query=blast_query,
                                subject_id=alignment.hit_def,
                                sstart=hsp.sbjct_start,
                                send=hsp.sbjct_end
                                )  # hsp.positives
                b.pub_date = timezone.now()
                b.save()
