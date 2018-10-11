from django.db import models
# get our timezone
from django.utils import timezone
# get users model
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    # TextField allow more space
    content = models.TextField()
    # DateTimeField options:-
    # -----------------------
    # auto_now_add=True on create
    # auto_now=True on update
    # default=timezone.now we path the function and not exec it
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # we added this function to get title when i print its object
    def __str__(self):
        return self.title
