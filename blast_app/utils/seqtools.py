# import unittest
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Nice to have: case id line/ multiple fasta formatted sequences

BIO_CHARACTERS = {"dna": set("ATGC")}
BIO_FORMATS = ["fasta"]


def clean_sequence(string):
    """
    Removes newlins/ linebreaks and spaces that could
    be inserted by copy/pasting.
    """
    return string.upper().replace("\n", "").replace("\r", "").replace(" ", "")


def check_bio_characters(seq_string, seq_type):
    """Checks sequence for allowed characters."""
    seq_string = clean_sequence(seq_string)
    allowed_nucleotides = BIO_CHARACTERS.get(seq_type)
    input_chars = set(seq_string)

    if input_chars != allowed_nucleotides:
        not_allowed = input_chars - allowed_nucleotides
        raise Exception("Input sequence contains invalid characters: {}\n \
                         allowed are: {}".format(not_allowed,
                                                 allowed_nucleotides))
    return seq_string


def write_bio_seq(seq_string, bio_id, seq_type,
                  bio_format, outfile, description):
    """Writes fasta sequence to specified path."""
    assert bio_format in BIO_FORMATS
    seq_string = check_bio_characters(seq_string,
                                      seq_type=seq_type)
    seq = Seq(seq_string)
    rec = SeqRecord(seq, id=bio_id, description=description)

    SeqIO.write(rec, outfile, bio_format)
