from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('planilla.apps.home.views',
	url(r'^acerca/$','acerca_view', name = 'vista_acerca'),
)