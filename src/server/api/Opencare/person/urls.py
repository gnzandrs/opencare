from django.conf.urls import url
from person import views

urlpatterns = [
    url(r'^person/$', views.JSONResponse.person_list),
    url(r'^person/(?P<pk>[0-9]+)/$', views.JSONResponse.person_detail)
]
