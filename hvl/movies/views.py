from django.views.generic import \
    CreateView, UpdateView, DeleteView, DetailView, ListView
from movies.forms import GenreForm, MovieForm
from django.urls.base import reverse_lazy
from movies.models import Genre, Movie


class MovieCreateView(CreateView):
    form_class = MovieForm
    template_name = "movie.html"
    success_url = reverse_lazy("movie-list")


class MovieListView(ListView):
    model = Movie
    template_name = "list.html"
    extra_context = {"detail_url": "movie-detail"}


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'update.html'
    success_url = reverse_lazy("movie-list")
    form_class = MovieForm


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "delete.html"
    success_url = reverse_lazy("movie-list")


class MovieDetailView(DetailView):
    model = Movie
    template_name = "detail.html"

