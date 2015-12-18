from django.conf.urls import patterns, include, url
from django.contrib import admin
from traceapp import views

urlpatterns = patterns('',
                      url(r'^$', views.loginHome, name='login'),
					  url(r'^admin/', include(admin.site.urls)),
					  url(r'^loginUser$', views.loginUser, name='loginUser'),
					  url(r'^logout$', views.logout, name='logout'),
					  url(r'^signUp$', views.signUp, name='signUp'),
					  url(r'^regItem$', views.regItem, name='regItem'),
					  url(r'^disable(?P<name>[^/]+)$', views.disable, name='disable'),
					  url(r'^(?P<userId>[^/]+)/?$', views.home, name='home'),
)
