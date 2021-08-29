from django.urls import path
from rate.views import RatingCreateView


urlpatterns = [
    path('rate/', RatingCreateView.as_view(), name='rate'),
    ]