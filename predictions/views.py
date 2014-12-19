import itertools, datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from predictions.forms import PredictionForm, UserForm
from predictions.models import Prediction, User

# class IndexView(generic.ListView):
#     template_name = 'predictions/index.html'
#     context_object_name = 'latest_predictions'

#     def get_queryset(self):
#         """Return the last five predictions"""
#         return Prediction.objects.order_by('-prediction_date')[:5]

def index(request):
    if request.user.is_authenticated():
        for prediction in itertools.chain(request.user.prediction_up.all(), request.user.prediction_down.all()):
            if prediction.is_expiring():
                messages.info(request, '{}: Expiring soon!'.format(prediction.prediction_text))
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p = Prediction(prediction_text=data['prediction'], deadline_date=data['deadline'])
            p.save()
        return HttpResponseRedirect(reverse('predictions:index'))
    else:
        form = PredictionForm()
        #latest_predictions = Prediction.objects.order_by('-up_votes')
        latest_predictions = Prediction.objects.exclude(deadline_date__lt=datetime.date.today()).order_by('deadline_date')
        return_dict = {'form': form, 'latest_predictions': latest_predictions}
    return render(request, 'predictions/index.html', return_dict) 


class DetailView(generic.DetailView):
    model = Prediction
    template_name = 'predictions/detail.html'


# class ResultsView(generic.DetailView):
#     model = Prediction
#     template_name = 'predictions/results.html'

def vote(request, prediction_id):
    if request.user.is_authenticated():
        p = get_object_or_404(Prediction, pk=prediction_id)
        # if request.POST['vote']: 
        if not p in request.user.prediction_up.filter(pk=p.pk) and not p in request.user.prediction_down.filter(pk=p.pk):
            if request.POST['vote'] == 'thumbs_up':
                request.user.prediction_up.add(p)
            if request.POST['vote'] == 'thumbs_down':
                request.user.prediction_down.add(p)
            p.save()    
        else:
            messages.info(request, 'Please only vote once per prediction.')
    else:
        messages.info(request, 'Please login to vote.')

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
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('predictions:index'))
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

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('predictions:index'))

@login_required
def user_profile(request, user):
    user = User.objects.get(username=user)
    return render(request, 'predictions/user.html', {'user': user})
