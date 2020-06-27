from django.urls import path

from django.views.generic.base import TemplateView
from www.views import FilmListView, FilmDetailView, FilmPosterListView


urlpatterns = [
    path('', FilmListView.as_view(),
        name='film_list'),
    path('poster/', FilmPosterListView.as_view(),
        name='film_poster_list'),
    path('login/', TemplateView.as_view(template_name='adminlte/login.html'),
        name='login'),
    path('<slug:slug>/', FilmDetailView.as_view(),
        name='film_details'),
]
