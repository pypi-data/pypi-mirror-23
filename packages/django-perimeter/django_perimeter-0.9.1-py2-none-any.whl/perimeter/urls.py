# -*- coding: utf-8 -*-
# urls for perimeter app.
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^gateway/',
        views.gateway,
        name='gateway'
    ),
]
