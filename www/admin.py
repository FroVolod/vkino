from django.contrib import admin

from .models import Category, Genre, Cinematographer, Film, FilmPicture


class FilmPictureAdmin(admin.TabularInline):
    model = FilmPicture
    extra = 1
    

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    inlines = [FilmPictureAdmin]

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Cinematographer)
admin.site.register(FilmPicture)
