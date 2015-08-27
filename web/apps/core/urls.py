from django.conf.urls import include, url
from django.contrib import admin
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

urlpatterns = [
    # url(r'/api/v1/', include(router.urls, namespace='api')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('allauth.urls')),
]
