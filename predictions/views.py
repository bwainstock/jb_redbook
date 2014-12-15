from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from predictions.models import Prediction

def index(request):
    latest_prediction_list = Prediction.objects.order_by('-prediction_date')[:5]
    context = {'latest_prediction_list': latest_prediction_list,}

    return render(request, 'predictions/index.html', context)

def detail(request, prediction_id):
    prediction = get_object_or_404(Prediction, pk = prediction_id)
    return render(request, 'predictions/detail.html', {'prediction': prediction})

def results(request, prediction_id):
    response = "You're looking at the results for prediction {}."
    return HttpResponse(response.format(prediction_id))

def vote(request, prediction_id):
    return HttpResponse("You're voting on question {}.".format(prediction_id))
