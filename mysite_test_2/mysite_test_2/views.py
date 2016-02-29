from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
import datetime
def hello_from_mysite_test_2(request):
	return HttpResponse("Hello world from mysite_test_2")

	#动态URL	
def dynamic_url_function(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)