from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from www.models import Film


class FilmListView(ListView):
    model = Film
    template_name = 'www/film_list.html'
    queryset = model.objects.all()


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
        film = Film.objects.get(slug=self.kwargs.get('slug'))
        return context
