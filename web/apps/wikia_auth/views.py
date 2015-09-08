# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from oauth2_provider.ext.rest_framework import TokenHasScope
from oauth2_provider.models import AccessToken
from rest_framework import views
from rest_framework import permissions
from rest_framework import response
import datetime


class TokenInfoView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope, ]
    required_scopes = ['read']

    def get(self, request, *args, **kwargs):
        access_token = AccessToken.objects.get(token=request.auth.token)

        return response.Response({
            'access_token': access_token.token,
            'expires_in': int((access_token.expires.replace(tzinfo=None)-datetime.datetime.now()).total_seconds()),
            'token_type': 'Bearer',
            'refresh_token': access_token.refresh_token.token,
            'scope': access_token.scope
        })
