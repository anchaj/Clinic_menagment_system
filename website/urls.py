from django.conf.urls import url, patterns
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'index.html', views.home),
    url(r'^clinic.html$', views.clinic),
    url(r'^doctor.html$', views.doctor),
    url(r'^pricing.html$', views.pricing),
    url(r'^contact.html$', views.contact),
    url(r'^register', views.register),
    url(r'^logout', views.logout_user),
    url(r'^authenticated.html', views.auth),
    url(r'^change_data.html', views.change_data)
]

urlpatterns += patterns("",
                        (r'^login', 'django.contrib.auth.views.login')
                        )
