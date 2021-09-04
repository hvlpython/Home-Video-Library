from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from movies.models import Genre, Movie
from rate.forms import RatingForm


class RatingCreateView(View):
    form_class = RatingForm
    template_name = "create.html"

    def post(self, request):
        print(request.POST)
        return HttpResponse("hrh")


    # def form_valid(self, form):
    #     print(form)
    #     return HttpResponse(content=form)

# testowa widok kategorii
# def view_product_category(request):
#     allmovies = Movie.objects.filter(name="Comedy")
#     print(allmovies)
#     print("//////////////")
#     #get average for each product within a category
#     return render(request, template_name="category.html", context={'allmovies': allmovies},
#     )