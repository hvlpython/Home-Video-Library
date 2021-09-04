from django.urls import path
from rate.views import RatingCreateView
from rate import views


urlpatterns = [
    path('rate/', RatingCreateView.as_view(), name='rate'),
    # path('genre/', views.view_product_category, name='genre'),
    ]