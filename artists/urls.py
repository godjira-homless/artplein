from django.urls import path
from artists import views
from artists.views import ArtistResults

urlpatterns = [
    path('', views.artists, name='artists'),
    path('search/', ArtistResults.as_view(), name='artist_search'),
    path('<int:id>/', views.artist_detail, name='artist_detail'),
    path('new_artist', views.new_artist, name='new_artist'),
    path('edit_artist/<int:id>', views.edit_artist, name='edit_artist'),
]