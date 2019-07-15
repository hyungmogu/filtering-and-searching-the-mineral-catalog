from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name="home"),
    url(r'^random/$', views.random_mineral, name="random"),
    url(r'^(?P<mineral_pk>\d+)/$', views.mineral_detail, name="mineral")
]
