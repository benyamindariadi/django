from django.conf.urls import url
from django.contrib.auth import views as auth_views
#django punya libs untuk view untuk login dan logout jadi gaperlu buat view secara manual.
from . import views

app_name = 'accounts'

#url untuk login, logout dan signup
urlpatterns = [
    url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'), #view dari django, diinject ke login.html
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"), #gaperlu template name krn ada dari libsnya
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
]
