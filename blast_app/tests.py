import os
import unittest

from pathlib import Path
from tempfile import TemporaryDirectory

from django.test import TestCase
from django.utils import timezone

from .models import BlastQuery, BlastResult
from .utils import seqtools as st


class SequenceToolsTest(unittest.TestCase):
    def test_wrong_character(self):
        with self.assertRaises(Exception):
            st.check_bio_characters("ATIHCASUI", seq_type="dna")

    def test_correct_sequence(self):
        seq = st.check_bio_characters("ATGAGC", seq_type="dna")
        self.assertEqual(seq, "ATGAGC")

    def test_fasta_write(self):
        test_seq = "ATGATCGATCGATCGTGACTGATCGTGACGCAGTGCAT"
        with TemporaryDirectory() as tmppath:
            outfile = Path(tmppath).joinpath("unittest_seq.fasta")
            st.write_bio_seq(test_seq,
                             bio_id="test_id",
                             seq_type="dna",
                             bio_format="fasta",
                             description="test_case",
                             outfile=str(outfile)
                             )
            os.path.isfile(str(outfile))


class BlastAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
            blast_query = BlastQuery(query_id="Test_blast",
                                     pub_date=timezone.now())
            blast_query.save()
            b = BlastResult(query=blast_query,
                            subject_id="test_hit",
                            sstart=10,
                            send=30
                            )
            b.pub_date = timezone.now()
            b.save()

    def test_blast_query(self):
        blast_query = BlastQuery.objects.get(id=1)
        self.assertEqual(str(blast_query.query_id), "Test_blast")

    def test_results(self):
        blast_query = BlastQuery.objects.get(id=1)
        results = blast_query.blastresult_set.all()[0]
        self.assertEqual(results.subject_id, "test_hit")
        self.assertEqual(results.sstart, 10)
        self.assertEqual(results.send, 30)
