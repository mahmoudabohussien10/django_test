# we took that from django urls.py
from django.urls import path
# . mean the same dir
# import views to use http request
from . import views
# route name to specify the route
urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]
