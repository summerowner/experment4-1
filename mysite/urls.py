from django.conf.urls import patterns, include, url
#from django.conf.urls import patterns,include, url
from django.contrib import admin
from libymanage.views import main,  signup, mainpage, search, add, loginsure, addauthor, shownews, delete, update, more 


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',main),
    url(r'^main/$',main),
  #  url(r'^sign/$', sign),
    url(r'^more/$',more),
     url(r'^signup/$', signup),
     url(r'^mainpage/$', mainpage),
     url(r'^search/(.*)$', search),
      url(r'^add/(.*)$', add),
        url(r'^login/$', loginsure),
 url(r'^addau/$', addauthor),
  url(r'^show/(.*)$', shownews),
url(r'^delete/(.*)$', delete),
url(r'^update/(.*)$', update),
     url(r'^admin/', include(admin.site.urls)),
)