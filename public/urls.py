from django.urls import path

from .frontend_api import SessionsAPI, AIShortener
from .views import AccountLogin, AccountRegister, Home, TalkToAI, MyFriend

app_name = "public"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("login", AccountLogin.as_view(), name="login"),
    path("signup", AccountRegister.as_view(), name="signup"),
    path("talk-to-ai", TalkToAI.as_view(), name="talk-to-ai"),
    path("my-friend", MyFriend.as_view(), name="my-friend"),
    path("ai-shortener", AIShortener.as_view(), name="ai-shortener"),
    # frontend_apis
    path("frontend-api/v1/sessions", SessionsAPI.as_view(), name="session-api"),
]
