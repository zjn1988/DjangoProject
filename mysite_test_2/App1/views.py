from django.shortcuts import render# 引用template index.html：方法2

# Create your views here. 【views】名字可以自定义
from django.http import HttpResponse				# 引用template index.html：方法1
from django.template import RequestContext, loader# 引用template index.html：方法2
from App1.models import T_Test_For_Django
	
def hello_from_App1(request):
	return HttpResponse("Hello world from app1")

#引用templates
def index(request):
#引用template index.html：方法1，测试可工作
	# T_Test_For_Django_list = T_Test_For_Django.objects.all()
	# template = loader.get_template('App1/index.html')
	# context = RequestContext(request, {
	# 'T_Test_For_Django_list': T_Test_For_Django_list,
	# })
	# return HttpResponse(template.render(context))
#引用template index.html：方法2，测试可工作
	T_Test_For_Django_list = T_Test_For_Django.objects.all()
	context = {'T_Test_For_Django_list': T_Test_For_Django_list}
	return render(request, 'App1/index.html', context)