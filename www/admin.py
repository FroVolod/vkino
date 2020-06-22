from django.contrib import admin

from .models import Category, Genre, Cinematographer, Film, FilmPicture


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Cinematographer)
admin.site.register(FilmPicture)
