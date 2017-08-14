# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^index.html$', views.HomePageView.as_view()),
    url(r'^about.html$', views.AboutPageView.as_view()),
    url(r'^contact.html$', views.ContactPageView.as_view()),
    url(r'^analyze.html$', views.AnalyzePageView.as_view()),
    url(r'^maps.html$', views.MapsPageView.as_view()),
]