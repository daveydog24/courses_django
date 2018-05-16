from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^course/destroy/(?P<id>\d+)$', views.results),
    url(r'^course/deletingcoursenumber(?P<id>\d+)$', views.delete),
    url(r'^course/add_course$', views.add_course),
    url(r'^clear$', views.clear),
    url(r'^', views.index)
]


