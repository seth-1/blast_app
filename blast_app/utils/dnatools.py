# import unittest
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Nice to have: case id line/ multiple fasta formatted sequences


def clean_sequence(string):
    return string.replace("\n", "").replace("\r", "").replace(" ", "")


def write_dna_seq(seq_string, fa_path):
    seq_string = clean_sequence(seq_string)
    allowed_nucleotides = set("ATGC")
    input_chars = set(seq_string)

    if input_chars != allowed_nucleotides:
        not_allowed = input_chars - allowed_nucleotides
        raise Exception("Input sequence contains invalid characters: {}\n \
                         allowed are: {}".format(not_allowed,
                                                 allowed_nucleotides))

    seq = Seq(seq_string)
    rec = SeqRecord(seq, id="id_here", description="User supplied seq")
    fa_path = fa_path.joinpath("test_it_sequence.fasta")

    SeqIO.write(rec, str(fa_path), format="fasta")
