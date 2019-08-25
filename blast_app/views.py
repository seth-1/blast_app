from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BlastQuery
from .serializers import BlastQuerySerializer
from .tasks import prepare_blast


class IndexView(generics.ListCreateAPIView):
    queryset = BlastQuery.objects.all()
    serializer_class = BlastQuerySerializer


@api_view(['POST'])
def blast_request(request):
    dna_sequence = request.data
    blast_res = prepare_blast.delay(seq=dna_sequence,
                                    db='blast_app/data/proteins.fasta')
    blast_res.wait(timeout=200, interval=0.5)
    return Response(status=status.HTTP_201_CREATED)
