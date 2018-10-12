# use redirect to redirect route by name
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# import flash messages
from django.contrib import messages
from .forms import UserRegisterForm
# login required decorator to use it on ur function to prevent unlogined users
from django.contrib.auth.decorators import login_required


# messages.debug()
# messages.info()
# messages.warning()
# messages.error()
# messages.success()

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # save form data to database
            form.save()
            # get request data from cleaned_data dict
            username = form.cleaned_data.get('username')
            # add new msg to flash
            messages.success(request, 'Your Account Has Been Created! You Are Now Able To Login.')
            # redirect to blog home page
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})
# decoration adds a functionality( code like : if or some checks ) to our function
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})
