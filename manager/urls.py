# -*- coding: utf-8 -*-
# @Author: Fannie

from django.conf.urls import url
from manager import views

app_name = 'manager'

urlpatterns = [
    url(r'^vmpzm/$', views.vmpzm, name='vmpzm'),
    url(r'^vmpzm/(?P<vmpzxx_id>[0-9]+)/rem/$', views.vmpzxx_rem, name='vmpzxx_rem'),
    url(r'^vmpzm/(?P<vmpzxx_id>[0-9]+)/change/$', views.vmpzxx_change, name='vmpzxx_change'),
    url(r'^vmpzm/batchrem/$', views.vmpzxx_batch_rem, name='vmpzxx_batch_rem'),
    url(r'^vmpzm/upload/$', views.upload, name='vmpzxx_upload'),
]