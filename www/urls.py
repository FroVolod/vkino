from django.urls import path

from www.views import (
    FilmListView, FilmDetailView, FilmPosterListView,
)


urlpatterns = [
    path('', FilmListView.as_view(),
        name='film_list'),
    path('poster/', FilmPosterListView.as_view(),
        name='film_poster_list'),
    path('<slug:slug>/', FilmDetailView.as_view(),
        name='film_details'),
]
