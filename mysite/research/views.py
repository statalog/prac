from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Study

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'research/index.html'
    context_object_name = 'latest_research_list'

    def get_queryset(self):
        """
        Return the last five published (not including those set to be
        published in the future).
        """
        return Study.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        

class DetailView(generic.DetailView):
    model = Study
    template_name = 'research/detail.html'

   # study = get_object_or_404(Study, id=pk)
   # study.add_seen()

class UploadView(generic.UploadView):
    model = Study
    template_name = 'research/upload.html'

class ResultsView(generic.DetailView):
    model = Study
    template_name = 'research/results.html'



       # selected_study.times_seen += 1
       # selected_study.save()
