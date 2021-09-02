from django.shortcuts import render
from django.views.generic import CreateView

from movies.models import Genre, Movie
from rate.forms import RatingForm


class RatingCreateView(CreateView):
    form_class = RatingForm
    template_name = "create.html"

# testowa widok kategorii
# def view_product_category(request):
#     allmovies = Movie.objects.filter(name="Comedy")
#     print(allmovies)
#     print("//////////////")
#     #get average for each product within a category
#     return render(request, template_name="category.html", context={'allmovies': allmovies},
#     )