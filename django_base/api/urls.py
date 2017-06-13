from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    url(r'inner/$', views.InnerList.as_view()),
    url(r'inner/(?P<pk>[0-9]+)/$', views.InnerDetail.as_view()),
])
