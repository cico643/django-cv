from django.conf.urls import url
from cv_Bilgi.views import *
app_name='cv_Bilgi'

urlpatterns = \
    [

    url(r'^index/$', bilgi_index, name='index'),
    url(r'^create/$', bilgi_create,name='create'),
    url(r'^(?P<slug>[\w-]+)/$', bilgi_detail,name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', bilgi_update,name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', bilgi_delete,name='delete'),
    ]
