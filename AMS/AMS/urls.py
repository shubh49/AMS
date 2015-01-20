from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('AMS.views',
    # Examples:
    # url(r'^$', 'AMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^infopage/','ainfopage'),
    url(r'^thanks','thnxs'),
    url(r'^ainfo/','ainfo'),
    url(r'^home/','home'),
    url(r'^departinfo','departinfo'),
    url(r'^depart','depart'),
    url(r'^test','test'),
    url(r'^arrinfo/','arrinfo'),
    url(r'^arrquery','arrquery'),
    url(r'^addinfo/','addinfo'),
    url(r'^addfun','addfun'),
    url(r'^login/','login'),
    url(r'^authuser','auth_user')
)
