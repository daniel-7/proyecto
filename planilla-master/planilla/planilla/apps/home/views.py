from django.shortcuts import render_to_response
from django.template import RequestContext

def acerca_view(request):
	return render_to_response('home/acerca.html',context_instance=RequestContext(request))
