from django.shortcuts import render

# Create your views here. 【views】名字可以自定义
from django.http import HttpResponse
	
def hello_from_App1(request):
	return HttpResponse("Hello world from app1")