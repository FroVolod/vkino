from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from datetime import date

from www.models import Film


class FilmListView(ListView):
    model = Film
    template_name = 'www/film_list.html'

    def get_context_data(self, **kwargs):
        context = super(FilmListView, self).get_context_data(**kwargs)
        film_list = self.model.objects.filter(flag_poster=False)
        context['film_list'] = film_list
        context['poster_1'] = film_list.last().poster.url
        context['film_poster_list'] = self.model.objects.filter(flag_poster=True)
        context['date_today'] = date.today()         
        return context


class FilmPosterListView(ListView):
    model = Film
    template_name = 'www/film_poster_list.html'

    def get_context_data(self, **kwargs):
        context = super(FilmPosterListView, self).get_context_data(**kwargs)
        context['film_poster_list'] = self.model.objects.filter(flag_poster=True)
        return context


class FilmDetailView(DetailView):
    model = Film
    template_name = 'www/film_detail.html'

    def dispatch(self, *args, **kwargs):
        object = self.get_object()
        return super(FilmDetailView, self).dispatch(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(
            Film,
            slug=self.kwargs.get('slug')
            )

    def get_context_data(self, *args, **kwargs):
        context = super(FilmDetailView, self).get_context_data(*args, **kwargs)
        film = self.model.objects.get(slug=self.kwargs.get('slug'))
        context['image_list'] = film.filmpicture_set.all()
        context['image_last'] = film.filmpicture_set.all().last().image.url
        return context
