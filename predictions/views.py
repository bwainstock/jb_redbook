from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from predictions.models import Prediction
from predictions.forms import PredictionForm

class IndexView(generic.ListView):
    template_name = 'predictions/index.html'
    context_object_name = 'latest_predictions'

    def get_queryset(self):
        """Return the last five predictions"""
        return Prediction.objects.order_by('-prediction_date')[:5]

def index(request):

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p = Prediction(prediction_text=data['prediction'], deadline_date=data['deadline'])
            p.save()

        return HttpResponseRedirect(reverse('predictions:index'))
    else:
        form = PredictionForm()
        latest_predictions = Prediction.objects.order_by('-thumbs_up')
        return_dict = {'form': form, 'latest_predictions': latest_predictions}
    return render(request, 'predictions/index.html', return_dict) 


class DetailView(generic.DetailView):
    model = Prediction
    template_name = 'predictions/detail.html'


class ResultsView(generic.DetailView):
    model = Prediction
    template_name = 'predictions/results.html'


def vote(request, prediction_id):
    p = get_object_or_404(Prediction, pk=prediction_id)
    # if request.POST['vote']: 
    if request.POST['vote'] == 'thumbs_up':
        p.thumbs_up += 1
    if request.POST['vote'] == 'thumbs_down':
        p.thumbs_down += 1

    p.save()    

    return HttpResponseRedirect(reverse('predictions:index'))

