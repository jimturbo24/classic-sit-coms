from django.conf.urls import url
from . import views

app_name = 'shows'
urlpatterns = [
    url(r'^shows/$', views.show_index, name="show-index" ),
    url(r'^shows/(?P<show_id>[0-9]+)/$', views.show_view, name='show-details'),

    url(r'^actors/$', views.actor_index, name="actor-index" ),
    url(r'^actors/(?P<actor_id>[0-9]+)/$', views.actor_view, name='actor-details'),

    url(r'^episodes/$', views.episode_index, name="episode-index" ),
    url(r'^episodes/(?P<episode_id>[0-9]+)/$', views.episode_view, name='episode-details'),

    url(r'^seasons/$', views.season_index, name="season-index" ),
    url(r'^seasons/(?P<season_id>[0-9]+)/$', views.season_view, name='season-details'),

    url(r'^characters/$', views.character_index, name="character-index" ),
    url(r'^characters/(?P<character_id>[0-9]+)/$', views.character_view, name='character-details'),

    url(r'^directors/$', views.director_index, name="director-index" ),
    url(r'^directors/(?P<director_id>[0-9]+)/$', views.director_view, name='director-details'),

    url(r'^reviews/$', views.review_index, name="review-index" ),
    url(r'^reviews/(?P<review_id>[0-9]+)/$', views.review_view, name='review-details'),

    url(r'^writers/$', views.writer_index, name="writer-index" ),
    url(r'^writers/(?P<writer_id>[0-9]+)/$', views.writer_view, name='writer-details'),

    url(r'^create-account/$', views.new_user, name="new-user" )
]
