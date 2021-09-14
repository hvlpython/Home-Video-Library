from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView,
)
from movies.forms import MovieForm, UpdateMovieForm
from django.urls.base import reverse_lazy
from movies.models import Movie
from accounts.views import IsUserNameMixin



class MovieCreateView(IsUserNameMixin, CreateView):
    form_class = MovieForm
    template_name = "movie.html"
    success_url = reverse_lazy("movie-list")


class MovieListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "list.html"
    extra_context = {"detail_url": "movie-detail"}


class MovieUpdateView(IsUserNameMixin, UpdateView):
    model = Movie
    template_name = "update.html"
    success_url = reverse_lazy("movie-list")
    form_class = UpdateMovieForm


class MovieDeleteView(IsUserNameMixin, DeleteView):
    model = Movie
    template_name = "delete.html"
    success_url = reverse_lazy("movie-list")


class MovieDetailView(IsUserNameMixin, DetailView):
    model = Movie
    template_name = "detail.html"


class MovieActionListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/action.html"
    queryset = Movie.objects.filter(genre_id=1)
    extra_context = {"detail_url": "movie-detail"}


class MovieComedyListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/comedy.html"
    queryset = Movie.objects.filter(genre_id=2)
    extra_context = {"detail_url": "movie-detail"}


class MovieDramaListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/drama.html"
    queryset = Movie.objects.filter(genre_id=3)
    extra_context = {"detail_url": "movie-detail"}


class MovieFantasyListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/fantasy.html"
    queryset = Movie.objects.filter(genre_id=4)
    extra_context = {"detail_url": "movie-detail"}


class MovieHorrorListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/horror.html"
    queryset = Movie.objects.filter(genre_id=5)
    extra_context = {"detail_url": "movie-detail"}


class MovieMysteryListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/mystery.html"
    queryset = Movie.objects.filter(genre_id=6)
    extra_context = {"detail_url": "movie-detail"}


class MovieRomanceListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/romance.html"
    queryset = Movie.objects.filter(genre_id=7)
    extra_context = {"detail_url": "movie-detail"}


class MovieThrillerListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/thriller.html"
    queryset = Movie.objects.filter(genre_id=8)
    extra_context = {"detail_url": "movie-detail"}


class MovieWesternListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/western.html"
    queryset = Movie.objects.filter(genre_id=9)
    extra_context = {"detail_url": "movie-detail"}


class MovieSciFiListView(IsUserNameMixin, ListView):
    model = Movie
    template_name = "genre/sci-fi.html"
    queryset = Movie.objects.filter(genre_id=10)
    extra_context = {"detail_url": "movie-detail"}
