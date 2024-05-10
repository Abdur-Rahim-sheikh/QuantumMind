from django.urls import path

from .views import AccountLogin, AccountRegister, Home

app_name = "public"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("login/", AccountLogin.as_view(), name="login"),
    path("register/", AccountRegister.as_view(), name="register"),
]
