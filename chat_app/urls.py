from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chat_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name': 'chat_app/logIn.html'}, name='logIn'),
    url(r'^login/', 'django.contrib.auth.views.login', 
        {'template_name': 'chat_app/logIn.html'}, name='logIn'),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logOut'),
    url(r'^signup/', signUp, name='signUp'),
    url(r'^home/', home, name='home'),
)