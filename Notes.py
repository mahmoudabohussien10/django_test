# Note: application may content more than one app EX:[ One For admin and one for Posts etc.. ]
# Note: thunder means double underscores
# ===========================================================================================================
# to run dev server:-
# --------------------
# python manage.py runserver
# ===========================================================================================================
# to create a new app:-
# ----------------------
# python manage.py startapp <app name>
# ===========================================================================================================
# create migrations changes:-
# ---------------------------
# python manage.py makemigrations
# ===========================================================================================================
# install migrations:-
# --------------------
# python manage.py migrate
# ===========================================================================================================
# view sql migrations code:-
# ---------------------------
# python manage.py sqlmigrate <app name> <migrate first four numbers>
# python manage.py sqlmigrate blog 0001
# ===========================================================================================================
# to create an Admin user to ur app:-
# ------------------------------------
# python manage.py createsuperuser
# ===========================================================================================================
# install mysql and mysqlconnector:-
# ------------------------------------
# conda install mysqlclient
# ===========================================================================================================
# open django shell which allow u to interact with django objects:-
# ------------------------------------------------------------------
# python manage.py shell
# --------------------------------------------------------------
# import models:-
# ----------------
# from django.contrib.auth.models import User
# from blog.models import Post
# --------------------------------------------------------------
# query with model:-
# -------------------
# User.objects.all()
# User.objects.first()
# User.objects.filter(username="admin")
# User.objects.filter(username="admin").first()
# user = User.objects.filter(username="admin").first()
# user
# user.id
# user.pk
# post_1 = Post(title="Blog 1",author=user,content='First post content')
# Post.objects.all()
# exit()
# post = Post.objects.first()
# ------------------------------------------------------------------
# gives u a user object
# ----------------------
# post.author
# post.author.email
# ---------------------------------------------------------------------------------------------
# if u want all post created by user django made it automatic by write user obj then _set like:
# ---------------------------------------------------------------------------------------------
# user =  post.author
# user.post_set.all()
# it automatic add this user id to author_id and auto save too
# user.post_set.create(title="Blog 2",content='second post content')
# ===========================================================================================================
# template docs:-
# ----------------
# https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#filters
# ===========================================================================================================




























