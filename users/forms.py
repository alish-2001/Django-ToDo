from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model

#sign up form
class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model=get_user_model()
    fields=('email','username', )

#change the user's info in admin panel
class CustomUserChangeFrom(UserChangeForm):
  class Meta:
    model=get_user_model()
    fields=('email','username', )


    