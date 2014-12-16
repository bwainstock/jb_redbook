from django.conf.urls import patterns, url

from predictions import views

urlpatterns = patterns('',
	# ex: /
	url(r'^$', views.index, name="index"),
	# ex: /4/
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	# ex: /4/results/
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	# ex: /4/vote/
	url(r'^(?P<prediction_id>\d+)/vote/$', views.vote, name='vote'),
        # ex: /register/
        url(r'^register/$', views.register, name='register'),
        # ex /login/
        url(r'^login/$', views.user_login, name='login'),
)
