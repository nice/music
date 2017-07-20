from django.conf.urls import include, url

urlpatterns = [
    url(r'^home$', 'app.views.home', name='home'),
]
