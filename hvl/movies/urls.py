from django.urls import path
from movies.views import \
    MovieCreateView, MovieListView, MovieUpdateView, MovieDetailView, MovieDeleteView, MovieSciFiListView, \
    MovieActionListView, MovieComedyListView, MovieDramaListView, MovieFantasyListView, MovieHorrorListView, \
    MovieMysteryListView, MovieRomanceListView, MovieThrillerListView, MovieWesternListView



urlpatterns = [
    path('movie-create/', MovieCreateView.as_view(), name='movie-create'),
    path('movie-list/', MovieListView.as_view(), name='movie-list'),
    path('movie-update/<pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie-delete/<pk>/', MovieDeleteView.as_view(), name='movie-delete'),
    path('movie-detail/<pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('action-movie-list/', MovieActionListView.as_view(), name='action-movie-list'),
    path('comedy-movie-list/', MovieComedyListView.as_view(), name='comedy-movie-list'),
    path('drama-movie-list/', MovieDramaListView.as_view(), name='drama-movie-list'),
    path('fantasy-movie-list/', MovieFantasyListView.as_view(), name='fantasy-movie-list'),
    path('horror-movie-list/', MovieHorrorListView.as_view(), name='horror-movie-list'), 
    path('mystery-movie-list/', MovieMysteryListView.as_view(), name='mystery-movie-list'),
    path('romance-movie-list/', MovieRomanceListView.as_view(), name='romance-movie-list'),
    path('thriller-movie-list/', MovieThrillerListView.as_view(), name='thriller-movie-list'),
    path('western-movie-list/', MovieWesternListView.as_view(), name='western-movie-list'),
    path('sci-fi-movie-list/', MovieSciFiListView.as_view(), name='sci-fi-movie-list'),
]
