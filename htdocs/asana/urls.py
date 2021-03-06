from feed import views
from feed.views import FeedViewSet,DataFieldViewSet,ValueStoreViewSet
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#REST FRAMEWORK
feed = FeedViewSet.as_view({
'get': 'list',
'post': 'create'
})

feed_detail = FeedViewSet.as_view({
	'get': 'retrieve',
})

field_list = DataFieldViewSet.as_view({
	'get': 'list'
}, renderer_classes=[renderers.StaticHTMLRenderer])

field_detail = DataFieldViewSet.as_view({
	'get': 'retrieve'
}, renderer_classes=[renderers.StaticHTMLRenderer])

value_list = ValueStoreViewSet.as_view({
	'get': 'list'
}, renderer_classes=[renderers.StaticHTMLRenderer])

value_detail = ValueStoreViewSet.as_view({
	'get': 'retrieve'
}, renderer_classes=[renderers.StaticHTMLRenderer])


urlpatterns = patterns('',
	#index
	url(r'^$', 'display.views.index', name='index'),

	#base template for layout
	url(r'^$', TemplateView.as_view(template_name='base.html')),

	#rest framework
	url(r'^api/$',feed,name='api_root'),
	url(r'^api/(?P<pk>[0-9]+)/$',feed_detail,name='feed-detail'),
  url(r'^api/(?P<pk>[0-9]+)/fields/$',field_list, name='field-list'),
  url(r'^api/(?P<pk>[0-9]+)/fields/(?P<fk>[0-9]+)/data$',value_list, name='value-list'),

	#rest Custom Feed
	url(r'^api/custom/(?P<id>[0-9]+)/$','feed.views.customFeed',name='customFeed'),

	#ipt app specific urls
	url(r'^indicators/', include('indicators.urls')),

	#enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	#enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	#home
	url(r'^home', 'display.views.listSilos', name='listSilos'),

	###READ
	#read init form
	url(r'^read', 'read.views.home', name='home'),

	#read init form
	url(r'^new_read', 'read.views.initRead', name='initRead'),

	#show read or source
	url(r'^show_read/(?P<id>\w+)/$', 'read.views.showRead', name='showRead'),

	#login form
	url(r'^login', 'read.views.getLogin', name='getLogin'),

	#getJSON data
	url(r'^json', 'read.views.getJSON', name='getJSON'),

	#updateUID data
	url(r'^update', 'read.views.updateUID', name='updateUID'),

	###DISPLAY
	#list all silos
	url(r'^silos', 'display.views.listSilos', name='listSilos'),

	#show silo detail and sources
	url(r'^silo/(?P<id>\w+)/$', 'display.views.viewSilo', name='viewSilo'),

	#merge form
	url(r'^merge/(?P<id>\w+)/$', 'display.views.mergeForm', name='mergeForm'),

	#merge select columns
	url(r'^merge_columns', 'display.views.mergeColumns', name='mergeColumns'),

	#list all silos
	url(r'^display', 'display.views.listSilos', name='listSilos'),

	#view silo detail
	url(r'^silo_detail/(?P<id>\w+)/$', 'display.views.siloDetail', name='siloDetail'),

	#edit single silo value
	url(r'^value_edit/(?P<id>\w+)/$', 'display.views.valueEdit', name='valueEdit'),

	#delete single silo value
	url(r'^value_delete/(?P<id>\w+)/$', 'display.views.valueDelete', name='valueDelete'),

	#edit single field
	url(r'^field_edit/(?P<id>\w+)/$', 'display.views.fieldEdit', name='fieldEdit'),


	###SILO
	url(r'^do_merge', 'silo.views.doMerge', name='doMerge'),

	#edit silo
	url(r'^silo_edit/(?P<id>\w+)/$', 'silo.views.editSilo', name='editSilo'),

	#merge silos
	url(r'^doMerge', 'silo.views.doMerge', name='doMerge'),

	#delete a silo
	url(r'^silo_delete/(?P<id>\w+)/$','silo.views.deleteSilo', name='deleteSilo'),

	###FEED
	url(r'^feed', 'feed.views.listFeeds', name='listFeeds'),

	#create a feed
	url(r'^create_feed', 'feed.views.createFeed', name='createFeed'),

	#delete a feed
	url(r'^feed_delete','feed.views.deleteFeed', name='deleteFeed'),

)

urlpatterns = format_suffix_patterns(urlpatterns)
