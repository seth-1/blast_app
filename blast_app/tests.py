import os
import unittest

from pathlib import Path
from tempfile import TemporaryDirectory

from django.test import TestCase

from .utils import seqtools as st

# TODO: remove file, generally run in temp directory
# Test BLAST in integration test
# Test BLAST in unittest


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

    # check that file exists
