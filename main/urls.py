from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),

    path('login/',views.loginView,name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/',views.signUp,name='signup'),
]