from django.shortcuts import render
from django.views.generic import CreateView
from rate.forms import RatingForm

class RatingCreateView(CreateView):
    form_class = RatingForm
    template_name = "create.html"
