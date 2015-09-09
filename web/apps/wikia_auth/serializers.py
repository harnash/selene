# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from datetime import datetime


class AccessTokenSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            "access_token": obj.token,
            "expires_in": int((obj.expires.replace(tzinfo=None)-datetime.now()).total_seconds()),
            "token_type": "Bearer",
            "refresh_token": obj.refresh_token.token,
            "scope": obj.scope,
        }
