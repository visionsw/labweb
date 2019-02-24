from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^searchresults/$", views.search, name="search"),
    url(r"^methods/(.+)/$", views.method_show)
]
urlpatterns += staticfiles_urlpatterns()