# use redirect to redirect route by name
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# import flash messages
from django.contrib import messages
from .forms import UserRegisterForm


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
            messages.success(request, 'Account Created For {}!'.format(username))
            # redirect to blog home page
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
