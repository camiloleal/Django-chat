from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chat_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', logIn),
    url(r'^login/', logIn),
    url(r'^signup/', signUp),
    url(r'^home/', home),
    url(r'^groups/', groups),
    url(r'^generalchat/', generalChat),
    url(r'^groupchat/', groupChat),
)