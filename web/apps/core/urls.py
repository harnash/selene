from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth/', include('wikia_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
