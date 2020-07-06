from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

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


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class MyLoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = "/"
    template_name = "registration/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(MyLoginFormView, self).form_valid(form)
