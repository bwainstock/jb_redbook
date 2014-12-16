from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login

from predictions.models import Prediction
from predictions.forms import PredictionForm, UserForm

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

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request, 'predictions/register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('predictions:index'))
            else:
                return HttpResponse('Your account is disabled.')

        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'predictions/login.html', {})
