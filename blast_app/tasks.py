from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory


from Bio.Blast.Applications import NcbiblastxCommandline

from celery import shared_task

from django.utils import timezone

from .models import BlastQuery, BlastResult
from .utils.seqtools import parse_blast_txt, write_bio_seq


@shared_task
def prepare_blast(seq, db, query_id="unknown", evalue=0.001):
    with TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)
            seq_file = tmppath.joinpath("tmp.fasta")
            blast_results_file = tmppath.joinpath('results.txt')

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
                                              outfmt=6,
                                              out=str(blast_results_file))
            blast_cmd()  # Running BLAST

            blast_result = parse_blast_txt(str(blast_results_file))

            for r in blast_result:
                b = BlastResult(query=blast_query,
                                subject_id=r.get("saccver"),
                                pident=Decimal(r.get("pident")),
                                length=r.get("length"),
                                mismatch=r.get("mismatch"),
                                gapopen=r.get("gapopen"),
                                qstart=r.get("qstart"),
                                qend=r.get("qend"),
                                sstart=r.get("sstart"),
                                send=r.get("send"),
                                evalue=Decimal(r.get("evalue")),
                                bitscore=Decimal(r.get("bitscore"))
                                )
                b.pub_date = timezone.now()
                b.save()
