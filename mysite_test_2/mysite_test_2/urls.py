from django.conf.urls import patterns, include, url
from django.contrib import admin
#from App1 import views
from App1.views import hello_from_App1
from mysite_test_2.views import hello_from_mysite_test_2
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite_test_2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello_1/$', hello_from_App1),#http://127.0.0.1:8000/hello_1/
	url(r'^hello_2/$', hello_from_mysite_test_2),#http://127.0.0.1:8000/hello_2/
)
