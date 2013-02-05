from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

from  auction import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'umc_auction.views.home', name='home'),
    # url(r'^umc_auction/', include('umc_auction.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='items'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auction/login.html'}),

    url(r'^bidders/?$', views.bidders, name='items'),
    url(r'^bidders/(?P<bidder_id>\d+)/?$', views.bidder, name='bidder'),
    url(r'^bidders/new/?$', views.new_bidder, name='new_bidder'),
    url(r'^bidders/(?P<bidder_id>\d+)/checkout/?$', views.checkout, name='checkout'),
    url(r'^bidders/(?P<bidder_id>\d+)/edit/?$', views.edit_bidder, name='edit_bidder'),
    url(r'^bidders/(?P<bidder_id>\d+)/delete/?$', views.delete_bidder, name='delete_bidder'),

    url(r'^items/?$', views.items, name='items'),
    url(r'^items/(?P<item_id>\d+)/?$', views.item, name='item'),
    url(r'^items/(?P<item_id>\d+)/delete/?$', views.delete_item, name='delete_item'),
    url(r'^items/(?P<item_id>\d+)/delete/?$', views.delete_item, name='delete_item'),
    url(r'^items/(?P<item_id>\d+)/edit/?$', views.edit_item, name='edit_item'),
    url(r'^items/new/?$', views.new_item, name='new_item'),
    url(r'^items/(?P<item_id>\d+)/purchase_item/?$', views.purchase_item, name='purchase_item'),

    url(r'^items/(?P<bidder_id>\d+)/purchases/(?P<purchase_id>\d+)/?$', views.purchase, name='purchase'),
    url(r'^items/(?P<bidder_id>\d+)/purchases/(?P<purchase_id>\d+)/delete/?$', views.delete_purchase, name='delete_purchase'),
)

urlpatterns += staticfiles_urlpatterns()
