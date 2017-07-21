from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from app.views import (TrackListView, TrackDetailView, TrackCreateView,
                       TrackUpdateView, GenreListView, GenreDetailView,
                       GenreCreateView, GenreUpdateView)

urlpatterns = [
    url(r'^tracks/$', TrackListView.as_view(), name='track-list'),
    url(r'^tracks/(?P<pk>\d+)/$', TrackDetailView.as_view(), name='track-detail'),
    url(r'^tracks/create/$', TrackCreateView.as_view(), name='track-create'),
    url(r'^tracks/(?P<pk>\d+)/update/$', TrackUpdateView.as_view(), name='track-update'),

    url(r'^genres/$', GenreListView.as_view(), name='genre-list'),
    url(r'^genres/(?P<pk>\d+)/$', GenreDetailView.as_view(), name='genre-detail'),
    url(r'^genres/create/$', GenreCreateView.as_view(), name='genre-create'),
    url(r'^genres/(?P<pk>\d+)/update/$', GenreUpdateView.as_view(), name='genre-update'),

    url(r'^$', RedirectView.as_view(url='/tracks/', permanent=False), name='index'),
]
