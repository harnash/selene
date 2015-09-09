# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from oauth2_provider.ext.rest_framework import TokenHasScope
from oauth2_provider.models import AccessToken
from rest_framework import generics
from rest_framework import permissions
from rest_framework import response
import datetime

from .serializers import AccessTokenSerializer


class TokenInfoView(generics.RetrieveAPIView):
    queryset = AccessToken.objects.all()
    serializer_class = AccessTokenSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasScope, ]
    required_scopes = ['read']
    lookup_field = 'token'

    def get_object(self):
        self.kwargs[self.lookup_field] = self.request.auth.token

        return super(TokenInfoView, self).get_object()
