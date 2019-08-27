import csv

from Bio import SeqIO
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


BIO_FORMATS = ["fasta"]
# BIO_CHARACTERS = {"dna": set("ATGC")}


def clean_sequence(string):
    """
    Removes newlins/ linebreaks and spaces that could
    be inserted by copy/pasting.
    """
    return string.upper().replace("\n", "").replace("\r", "").replace(" ", "")


# def check_bio_characters(seq_string, seq_type):
#     """Checks sequence for allowed characters."""
#     seq_string = clean_sequence(seq_string)
#     allowed_nucleotides = BIO_CHARACTERS.get(seq_type)
#     input_chars = set(seq_string)

#     if input_chars != allowed_nucleotides:
#         not_allowed = input_chars - allowed_nucleotides
#         raise Exception("Input sequence contains invalid characters: {}\n \
#                          allowed are: {}".format(not_allowed,
#                                                  allowed_nucleotides))
#     return seq_string


def write_bio_seq(seq_string, bio_id,
                  bio_format, outfile, description):
    """Writes fasta sequence to specified path."""
    assert bio_format in BIO_FORMATS
    seq = Seq(seq_string)
    rec = SeqRecord(seq, id=bio_id, description=description)

    SeqIO.write(rec, outfile, bio_format)


def parse_blast_txt(blast_file_path):
    """
    Parses blast in tabular format when run with outfmt 6.
    qaccver means Query accesion.version
    saccver means Subject accession.version
    pident means Percentage of identical matches
    length means Alignment length
    mismatch means Number of mismatches
    gapopen means Number of gap openings
    qstart means Start of alignment in query
    qend means End of alignment in query
    sstart means Start of alignment in subject
    send means End of alignment in subject
    evalue means Expect value
    bitscore means Bit score
    """
    header = ["qaccver", "saccver", "pident",
              "length", "mismatch", "gapopen",
              "qstart", "qend", "sstart", "send",
              "evalue", "bitscore"]
    with open(blast_file_path, "rt") as blastfile:
        blast_csv = csv.reader(blastfile, delimiter="\t")
        return [dict(zip(header, line)) for line in blast_csv]


def parse_blast_xml(blast_file_path):
    """
    Parses blast xml documents using the hsp object inside alignments.
    """
    result_hsps = []
    with open(str(blast_file_path)) as xml_handle:
        blast_rec = NCBIXML.read(xml_handle)
        for alignment in blast_rec.alignments:
            for hsp in alignment.hsps:
                result_hsps.append(hsp)

    return result_hsps
