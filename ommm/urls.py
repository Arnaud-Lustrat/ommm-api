from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'ommm'
urlpatterns = [

    # Authentification
    url(r'^signup/', views.SignUp.as_view()),
    url(r'^signin/', obtain_jwt_token),

    # Profile
    url(r'^profile/$', views.Profile.as_view()),

    # New fav
    url(r'^fav/$', views.Favoris.as_view()),

    # Types
    url(r'^types/$', views.TypesList.as_view()),
    url(r'^types/(?P<pk>[0-9]+)/$', views.TypesDetail.as_view()),

    # Tags
    url(r'^tags/$', views.TagsList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagsDetail.as_view()),

    # Exercises
    url(r'^exercises/$', views.ExercisesList.as_view()),
    url(r'^exercises/(?P<pk>[0-9]+)/$', views.ExercisesDetail.as_view()),

    # Subscriptions
    url(r'^subscriptions/$', views.SubscriptionsList.as_view()),
    url(r'^subscriptions/(?P<pk>[0-9]+)/$', views.SubscriptionsDetail.as_view()),

    # Sessions
    url(r'^sessions/$', views.SessionsList.as_view()),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionsDetail.as_view()),

    # Favs
    #url(r'^favs/$', views.FavsList.as_view()),
    #url(r'^favs/(?P<pk>[0-9]+)/$', views.FavsDetail.as_view()),

    # List Type with Exercises
    url(r'^list/$', views.List.as_view()),
    #url(r'^fav/$', views.Fav.as_view()),

    # Documentation
    url(r'^docs/', views.SwaggerSchemaView.as_view(), name='doc'),
]