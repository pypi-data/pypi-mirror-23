# -*- coding: utf-8 -*-
from django.conf.urls import url
from arrogant import views

urlpatterns = [
  url(r'^get/recommendJvalue$', views.recommendJvalue, name='recommendJvalue'),
  url(r'^get/jvalue$', views.jvalue, name='jvalue'),
  url(r'^get/jlist$', views.jlist, name='jlist'),
  url(r'^get/comment$', views.comment, name='comment'),
  url(r'^get/jcategory$', views.jcategory, name='jcategory'),
  url(r'^get/search$', views.search, name='search'),
  url(r'^post/like$', views.like, name='like'),
  url(r'^post/questionnaire$', views.questionnaire, name='questionnaire'),
]
