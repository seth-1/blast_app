from pathlib import Path

from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import BlastQuery
from .tasks import prepare_blast
from .utils.seqtools import write_bio_seq


class IndexView(generic.ListView):
    template_name = 'blast_app/index.html'
    context_object_name = 'blast_list'

    def get_queryset(self):
        """Return last blast results."""
        return BlastQuery.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


class ResultsView(generic.DetailView):
    model = BlastQuery
    template_name = 'blast_app/results.html'


def blast_request(request):
    dna_sequence = request.POST.get("dna_sequence", "")
    st.write_bio_seq(dna_sequence, Path("blast_app/data"))

    prepare_blast.delay()
    # do blast here
    return HttpResponseRedirect(reverse('blast_app:index'))
