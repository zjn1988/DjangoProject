from django.conf.urls import patterns, include, url
from django.contrib import admin
#from App1 import views
from App1.views import hello_from_App1
from mysite_test_2.views import hello_from_mysite_test_2
from mysite_test_2.views import dynamic_url_function

#from django.conf.urls.defaults import *
#from django.views.generic import list_detail
#from django.views.generic import *
from  django.views.generic import list
from App1.models import T_Test_For_Django
from django.http import HttpResponse
from App1.views import index

class Test_For_Django(list.ListView):
	def get(self,request):
		return HttpResponse(T_Test_For_Django.objects.all())
# = {
    # 'queryset': T_Test_For_Django.objects.all(),
# }

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite_test_2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	#普通URL
	url(r'^hello_1/$', hello_from_App1),#http://127.0.0.1:8000/hello_1/
	url(r'^hello_2/$', hello_from_mysite_test_2),#http://127.0.0.1:8000/hello_2/
	#动态URL
	url(r'^(\d{1,3})/$', dynamic_url_function),
	#动态URL
	url(r'^publishers/$', Test_For_Django.as_view(), name="1"),
	#配合templates使用
	url(r'^App1_List/$', index),
)
