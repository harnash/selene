# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from oauth2_provider.ext.rest_framework import TokenHasScope
from oauth2_provider.models import AccessToken
from rest_framework import generics
from rest_framework import permissions
from django.core import cache
from rest_framework_extensions.cache.decorators import (
    cache_response
)
from .serializers import AccessTokenSerializer


class TokenInfoView(generics.RetrieveAPIView):
    queryset = AccessToken.objects.all()
    serializer_class = AccessTokenSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasScope, ]
    required_scopes = ['read']
    lookup_field = 'token'

    @cache_response(1)
    def get(self, request, *args, **kwargs):
        return super(TokenInfoView, self).get(request, *args, **kwargs)

    def get_object(self):
        self.kwargs[self.lookup_field] = self.request.auth.token

        return super(TokenInfoView, self).get_object()
