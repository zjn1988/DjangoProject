from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
	
def hello_from_mysite_test_2(request):
	return HttpResponse("Hello world from mysite_test_2")