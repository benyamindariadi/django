from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm): #form for signup, formnya template dari django
    class Meta:
        fields = ("username", "email", "password1", "password2") # password 1,2 for authorization, liat documentation untuk daftar input lainnya
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name" #kasih label Display name untuk username untuk ditampilin di html
        self.fields["email"].label = "Email address" #kasih label Email address untuk email untuk ditampilin di html
