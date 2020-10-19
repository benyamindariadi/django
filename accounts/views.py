from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView): #view untuk signup 
    form_class = forms.UserCreateForm #hubungin ke form untuk signup
    success_url = reverse_lazy("login") #redirect kalo berhasil signup ke halaman untuk login
    template_name = "accounts/signup.html" #inject to signup.html
