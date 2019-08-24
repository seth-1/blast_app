import os
import unittest

from pathlib import Path

from django.test import TestCase

from .utils import seqtools as st

# TODO: remove file, generally run in temp directory


class SequenceToolsTest(unittest.TestCase):
    def test_wrong_character(self):
        with self.assertRaises(Exception):
            st.check_bio_characters("ATIHCASUI", seq_type="dna")

    def test_correct_sequence(self):
        seq = st.check_bio_characters("ATGAGC", seq_type="dna")
        self.assertEqual(seq, "ATGAGC")

    def test_fasta_write(self):
        test_seq = "ATGATCGATCGATCGTGACTGATCGTGACGCAGTGCAT"
        result_path = Path(
            "blast_app/data").joinpath("unit_test_sequence.fasta")
        st.write_bio_seq(test_seq,
                         bio_id="test_id",
                         seq_type="dna",
                         bio_format="fasta",
                         description="test_case",
                         outfile=str(result_path)
                         )
        os.path.isfile(str(result_path))

    # check that file exists
