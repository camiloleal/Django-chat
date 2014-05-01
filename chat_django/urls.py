from django.conf.urls import patterns, include, url
from chat_app.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chat_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicioSesion),
    url(r'^inicio/', inicio),
    url(r'^grupos', grupos),
    url(r'^chatgeneral', chatGeneral),
    url(r'^chatgrupo', chatGrupo),
)
