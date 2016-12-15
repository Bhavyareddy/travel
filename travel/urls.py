from django.conf.urls import include, url
from django.contrib import admin
from indra import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'travel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',include(admin.site.urls)),
    url(r'^bus/$',include(indra.views.passenger_list)),
    url(r'^bus/(?P<id>[\w\-]+)/$',include(indra.views.passenger_details)),
    url(r'^login/$','application.views.passenger_login'),
    url(r'^facebook/','application3.views.passenger_facebook'),
    url(r'^username/','application3.views.passenger_login')

]