from celery import shared_task

from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast import NCBIXML

@shared_task
def my_add_task(a, b):
    return a + b

@shared_task
def prepare_blast(query='blast_app/data/test_sequence.fasta', db='blast_app/data/proteins.fasta', evalue=0.001):
    blast_cmd = NcbiblastxCommandline(query=query, db=db, evalue=evalue)
    # blast_cmd = NcbiblastxCommandline(query=query, db=db, evalue=evalue, outfmt=5, out='results.xml')
    blast_print = blast_cmd()
    print(blast_print)

    # BlastResult("xml...").save()