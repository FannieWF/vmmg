# -*- coding: utf-8 -*-
# @Author: Fannie

from django.conf.urls import url
from iden import views

app_name = 'iden'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
