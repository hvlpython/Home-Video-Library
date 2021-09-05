from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse

from movies.models import Genre, Movie
from rate.forms import RatingForm
from rate.models import Rating


class RatingCreateView(View):
    form_class = RatingForm
    template_name = "create.html"

    def post(self, request):
        Rating.objects.create(movie_id=request.POST['movie'], rating=request.POST['rating'])
        return HttpResponseRedirect(reverse('movie-detail', args=[request.POST['movie']]))
