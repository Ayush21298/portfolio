from django.conf.urls import url
from . import views

urlpatterns=[ url(r'^(?P<entry_no>[0-9]+)/$',views.info,name='info'), url(r'^$',views.index,name='index'),  ]