# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from .views import TokenInfoView


urlpatterns = [
    url(r'^info$', TokenInfoView.as_view()),
]
