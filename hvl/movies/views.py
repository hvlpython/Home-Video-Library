from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from movies.forms import MovieForm
from django.urls.base import reverse_lazy
from movies.models import Movie


class MovieCreateView(CreateView):
    form_class = MovieForm
    template_name = "movie.html"
    success_url = reverse_lazy("movie-list")


class MovieListView(TemplateView):
    model = Movie
    template_name = "list.html"
    extra_context = {"movies" : Movie.objects.all()}


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'update.html'
    success_url = reverse_lazy("movie-list")
    form_class = MovieForm


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "delete.html"
    success_url = reverse_lazy("movie-list")
    