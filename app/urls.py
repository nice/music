from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from app.views import TrackListView, TrackDetailView, GenreListView, GenreDetailView


urlpatterns = [
    url(r'^tracks/$', TrackListView.as_view(), name='track-list'),
    url(r'^tracks/(?P<pk>\d+)/$', TrackDetailView.as_view(), name='track-detail'),
	url(r'^genres/$', GenreListView.as_view(), name='genre-list'),
    url(r'^genres/(?P<pk>\d+)/$', GenreDetailView.as_view(), name='genre-detail'),

    url(r'^$', RedirectView.as_view(url='/tracks/', permanent=False), name='index'),
]
