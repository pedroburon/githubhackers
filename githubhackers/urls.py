from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from userprofiles.views import auth_logout


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'', include('social_auth.urls')),
    url(r'^logout/', auth_logout, name='logout'),

    url(r'^profiles/', include('profiles.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
