from pathlib import Path
from tempfile import TemporaryDirectory

from Bio.Blast import NCBIXML
from Bio.Blast.Applications import NcbiblastxCommandline

from celery import shared_task

from django.utils import timezone

from .models import BlastQuery, BlastResult
from .utils.seqtools import write_bio_seq


@shared_task
def prepare_blast(seq, db, query_id="unknown", evalue=0.001):
    with TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            seq_file = tmppath.joinpath("tmp.fasta")
            blast_results_file = tmppath.joinpath('results.xml')

            write_bio_seq(seq,
                          bio_id="bio_id",
                          seq_type="dna",
                          bio_format="fasta",
                          description="test_app",
                          outfile=str(seq_file))

            blast_query = BlastQuery(query_id=query_id,
                                     pub_date=timezone.now())
            blast_query.save()

            blast_cmd = NcbiblastxCommandline(query=str(seq_file),
                                              db=db,
                                              evalue=evalue,
                                              outfmt=5,
                                              out=str(blast_results_file))
            blast_cmd()  # Running BLAST

            with open(str(blast_results_file)) as xml_handle:
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
