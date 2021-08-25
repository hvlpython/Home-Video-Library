from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from movies.forms import MovieForm
from django.urls.base import reverse_lazy
from movies.models import Movie


class MovieCreateView(CreateView):
    form_class = MovieForm
    template_name = "movie.html"
    success_url = reverse_lazy("movie-list")


class MovieListView(ListView):
    Model = Movie
    template_name = "movie.html"
    queryset = Movie.objects.all()


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'update.html'
    success_url = reverse_lazy("movie-list")
    form_class = MovieForm


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "delete.html"
    success_url = reverse_lazy("movie-list")