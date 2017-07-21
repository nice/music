from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

from app.models import Track, Genre


class TrackListView(ListView):
    model = Track
    paginate_by = 8

    def get_context_data(self, **kwargs):
    	context = super(TrackListView, self).get_context_data(**kwargs)
        return context


class TrackDetailView(DetailView):
    model = Track

    def get_context_data(self, **kwargs):
        context = super(TrackDetailView, self).get_context_data(**kwargs)
        return context


class TrackCreateView(CreateView):
    model = Track
    fields = ['title', 'rating', 'genres']

    def get_success_url(self):
        return reverse('app:track-list')


class TrackUpdateView(UpdateView):
    model = Track
    fields = ['title', 'rating', 'genres']

    def get_success_url(self):
        return reverse('app:track-detail', kwargs={'pk': self.object.pk})


class GenreListView(ListView):
    model = Genre

    def get_context_data(self, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        return context


class GenreDetailView(DetailView):
    model = Genre

    def get_context_data(self, **kwargs):
        context = super(GenreDetailView, self).get_context_data(**kwargs)
        return context


class GenreCreateView(CreateView):
    model = Genre
    fields = ['name']

    def get_success_url(self):
        return reverse('app:genre-list')


class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name']

    def get_success_url(self):
        return reverse('app:genre-detail', kwargs={'pk': self.object.pk})
