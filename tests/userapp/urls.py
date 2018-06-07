# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns('userapp.views',
    url(r'^pages/([\w\d-]+)/', 'page_detail', name="userapp_page_detail"),
    url(r'^products/(\d+)/', 'product_detail', name="userapp_product_detail"),
    url(r'^tags/(.+)/', 'tag_detail', name="userapp_tag"),
    url(r'^my/view/(.+)/', 'my_view', name="userapp_my_view"),
    url(r'^my/other/view/(.+)/', 'my_other_view', name="userapp_my_other_view"),
)
