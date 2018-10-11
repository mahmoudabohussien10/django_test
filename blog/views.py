from django.shortcuts import render
from .models import Post
# import response
from django.http import HttpResponse


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
        'title':"Blogs"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title':"About"
    }
    return render(request, 'blog/about.html', context)
