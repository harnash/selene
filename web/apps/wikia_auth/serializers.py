# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers


class AccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255, source='token')
    expires_in = serializers.DateTimeField(source='expires')
    # token_type = serializers.CharField(max_length=100)
    refresh_token = serializers.CharField(max_length=255)
    scope = serializers.CharField(allow_blank=True)
