from django.urls import path
from movies.views import MovieCreateView, MovieListView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('movie-create/', MovieCreateView.as_view(), name='movie-create'),
    path('movie-list/', MovieListView.as_view(), name='movie-list'),
    path('movie-update/<pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie-delete/<pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    ]
    