from django.urls import path

from .frontend_api import SessionsAPI
from .views import AccountLogin, AccountRegister, Home, TalkToAI

app_name = "public"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("login/", AccountLogin.as_view(), name="login"),
    path("signup/", AccountRegister.as_view(), name="signup"),
    path("talk-to-ai/", TalkToAI.as_view(), name="talk-to-ai"),
    # frontend_apis
    path("frontend-api/v1/sessions/", SessionsAPI.as_view(), name="session-api"),
]
