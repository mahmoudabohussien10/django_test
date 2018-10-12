"""new_jango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# we added include to add new apps Urls
from django.urls import path, include
from users import views as user_view
from django.contrib.auth import views as auth_views
# these both import to view user profile images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # add prefix and include urls of ur app
    # if we requested for this url it matches the first string pattern (blog/) then cut the rest and search for it in
    # included file "blog.urls" then preform an action

    # Note: at the end of each url we add ( / ) because by default django redirect
    # the route to route that ends with ( / )
    # path('blog/', include('blog.urls')),
    path('', include('blog.urls')),

    # we used the view directly of users
    path('register/', user_view.register, name="register"),
    # this way of using views called class based Views "auth_views.LoginView.as_view"
    # we can pass template name to the view to make our design to the html
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', user_view.profile, name="profile"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
