from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'participant')

class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'participant')