from pathlib import Path

from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# from django.utils import timezone
# from django.views import generic

from rest_framework import generics

from .models import BlastQuery
from .serializers import BlastQuerySerializer
from .tasks import prepare_blast
from .utils.seqtools import write_bio_seq


class IndexView(generics.ListCreateAPIView):
    # class IndexView(generic.ListView):
    queryset = BlastQuery.objects.all()
    serializer_class = BlastQuerySerializer
    # template_name = 'blast_app/index.html'
    # context_object_name = 'blast_list'

    # def get_queryset(self):
    #     """Return last blast results."""
    #     return BlastQuery.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:10]


class ResultsView(generics.RetrieveUpdateDestroyAPIView):
    pass
    # class ResultsView(generic.DetailView):
    # queryset = BlastResult.objects.all() 1st try
    # lookup_field = 'id'
    # tmpset = BlastQuery.objects.all()
    # queryset = tmpset.blastresult_set.all()
    # serializer_class = BlastResultSerializer
    # model = BlastQuery
    # template_name = 'blast_app/results.html'


def blast_request(request):
    dna_sequence = request.POST.get("dna_sequence", "")
    write_bio_seq(dna_sequence, Path("blast_app/data"))

    prepare_blast.delay()
    # do blast here
    return HttpResponseRedirect(reverse('blast_app:index'))
