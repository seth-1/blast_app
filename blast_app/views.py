from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BlastQuery
from .serializers import BlastQuerySerializer
from .tasks import prepare_blast
from .utils.seqtools import clean_sequence


class IndexView(generics.ListCreateAPIView):
    queryset = BlastQuery.objects.all()
    serializer_class = BlastQuerySerializer


# dna_sequence = check_bio_characters(dna_sequence,
#                                 seq_type="dna")
@api_view(['POST'])
def blast_request(request):
    dna_sequence = request.data
    print("Submitted dna sequence: {}".format(dna_sequence))
    if not dna_sequence:
        Response(status=status.HTTP_400_BAD_REQUEST)

    dna_sequence = clean_sequence(dna_sequence)
    allowed_nucleotides = set("ATGC")
    input_chars = set(dna_sequence)

    if input_chars != allowed_nucleotides:
        not_allowed = input_chars - allowed_nucleotides
        print("Input sequence contains invalid characters: {}\n \
                         allowed are: {}".format(not_allowed,
                                                 allowed_nucleotides))
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        blast_res = prepare_blast.delay(seq=dna_sequence,
                                        db='blast_app/data/proteins.fasta')
        blast_res.wait(timeout=200, interval=0.5)
        return Response(status=status.HTTP_201_CREATED)
