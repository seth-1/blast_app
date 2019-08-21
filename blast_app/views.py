from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .tasks import prepare_blast
from .models import BlastResult


class IndexView(generic.ListView):
    template_name = 'blast_app/index.html'
    context_object_name = 'blast_list'

    def get_queryset(self):
        """Return last blast results."""
        return BlastResult.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class ResultsView(generic.DetailView):
    model = BlastResult
    template_name = 'blast_app/results.html'

def blast_request(request):
    question_text = request.POST.get("question_text","")
    prepare_blast.delay()
    # do blast here
    return HttpResponseRedirect(reverse('blast_app:index'))