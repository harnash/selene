from django.conf.urls import include, url
from django.contrib import admin
# from rest_framework.routers import DefaultRouter

# from apps.facebook.views import FacebookLogin

# router = DefaultRouter()

urlpatterns = [
    # url(r'/api/v1/', include(router.urls, namespace='api')),

    url(r'^api-wikia_auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^rest-wikia_auth/', include('rest_auth.urls')),
    # url(r'^rest-wikia_auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^rest-wikia_auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth/', include('wikia_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('allauth.urls')),
]
