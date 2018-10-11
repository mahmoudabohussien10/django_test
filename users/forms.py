from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # by default EmailField is required we can change this by pass a param
    # required=false
    email = forms.EmailField()

    # Meta class gives us configurations(vars) for our model and form
    class Meta:
        # specify the model we want to interact with
        model = User
        # field shown in our form in order
        fields = ['username','email','password1','password2']