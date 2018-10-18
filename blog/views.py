# get_object_or_404 return 404 if user is not found in the query
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
# import response
from django.http import HttpResponse
# import a list view from generic handels to much logic and ui for us
# we can add parencese () to our import to make it in more than one line
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# instead of function decorator we can't use it on class so we use "LoginRequiredMixin" and make our class inherit it
# UserPassesTestMixin is to specify if the user is the owner of the post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# home Method must contain request even not used

# to make a template django looks for templates folder and then looking for a folder
# that has the same name as the app ( this the way of django works )
# blog -> templates -> blog -> template.html
# posts=[
#     {
#         'author':"mahmoud abo hussien",
#         'title':'Blog Post 1',
#         'content':'First post content',
#         'date_post': 'Aug 27, 2018'
#     },
#     {
#         'author':"Ahmed",
#         'title':'Blog Post 2',
#         'content':'Second post content',
#         'date_post': 'Aug 27, 2018'
#     },
# ]
def home(request):
    # return HttpResponse("<h1>Blog home</h1>")
    context = {
        'posts': Post.objects.all(),
        'title': "Blogs"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context)


# this class to view posts in home page
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    # we need to make a name for the variable (which hold all db objects) we will use in Home.html
    # we use context_object_name attribute
    # if we didn't add name we can use "object" in the view its the default name
    context_object_name = "posts"
    # to order the data that comes from db we use ordering attribute
    # this will order the data from oldest to newest
    # if we want to change it to be from newest to oldest we add (-) as a prefix to our col name
    ordering = ["-date"]
    # set pagination number
    paginate_by = 5

# get post that written by this user
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5
    def get_queryset(self):
        # kwargs is the query params
        user = get_object_or_404(User,username= self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by('-date')


# this class used to view one post details
class PostDetailView(DetailView):
    # "<app>/<model>_<view type>.html"
    # if we didn't add name we can use "object" in the view its the default name
    model = Post


# this class used to Create one post, LoginRequiredMixin to add auth when user try to use this route
# Note: the arrangement of inheretance is important to check auth at the first
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # add author id by override supper method form_valid to add our user then
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# update a post
# Note: the arrangement of inheretance is important to check auth at the first then if the user is the owner of the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # add author id by override supper method form_valid to add our user then
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # test_func return true or false to continue submit
    def test_func(self):
        # this method is used to get info about post we need to update
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # redirect in case of success to home page
    success_url = '/'
    def test_func(self):
        # this method is used to get info about post we need to update
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False













