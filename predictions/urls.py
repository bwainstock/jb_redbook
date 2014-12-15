from django.conf.urls import patterns, url

from predictions import views

urlpatterns = patterns('',
	# ex: /
	url(r'^$', views.index, name="index"),
	# ex: /4/
	url(r'^(?P<prediction_id>\d+)/$', views.detail, name='detail'),
	# ex: /4/results/
	url(r'^(?P<prediction_id>\d+)/results/$', views.results, name='results'),
	# ex: /4/vote/
	url(r'^(?P<prediction_id>\d+)/vote/$', views.vote, name='vote'),
)
