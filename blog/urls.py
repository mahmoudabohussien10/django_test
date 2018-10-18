# we took that from django urls.py
from django.urls import path
# . mean the same dir
# import views to use http request
from . import views
# route name to specify the route

# use our class view to render blog page
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    # class views must return a view so we use ( as_view() ) to do that
    # Note that class view need to have main template which always be in this form "<app>/<model>_<view type>.html"
    #  Or u can change this redirection it To ur layout
    # "<app>/<model>_<view type>.html" => app: is whole app name = blog, model: is the small app inside our project test_blog,
    # view type: is [ list or details or ... ]
    path('', PostListView.as_view(), name="blog-home"),
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    # this route to view details about a specific post using its primary key ( id )
    # we use <int:pk> to pass prams to our class [int : means it will be integer] and [pk means that we will pass primary key]
    # we can use any var instead of (pk) but we will add attribute in our class to define it
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-details"),
    # create new post
    path('post/new/', PostCreateView.as_view(), name="blog-create"),
    # update a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
    # get user posts
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),

]
