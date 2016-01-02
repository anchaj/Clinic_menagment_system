from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^index.html$', views.home),
    url(r'^clinic.html$', views.clinic),
    url(r'^doctor.html$', views.doctor),
    url(r'^pricing.html$', views.pricing),
    url(r'^contact.html$', views.contact)
]