from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path(r'play/<int:song_id>/', views.play_song, name='play_song'),
    path("upload/",views.upload_song, name='upload_song'),
    path("search/",views.search_song, name='search_song'),
    path("search_results/",views.search_results, name='search_results'),
    path("search_results/all/",views.all_songs, name='all_songs'),
]
