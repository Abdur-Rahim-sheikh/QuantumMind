from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .api import SessionsAPI, AIShortenerAPI
from .views import AccountLogin, AccountRegister, Home, TalkToAI, MyFriend

app_name = "public"

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("login", AccountLogin.as_view(), name="login"),
    path("signup", AccountRegister.as_view(), name="signup"),
    path("talk-to-ai", TalkToAI.as_view(), name="talk-to-ai"),
    path("my-friend", MyFriend.as_view(), name="my-friend"),

    # frontend_apis
    path("api/v1/sessions", SessionsAPI.as_view(), name="session-api"),
    path("api/v1/ai-shortener", csrf_exempt(AIShortenerAPI.as_view()), name="ai-shortener"),
]
