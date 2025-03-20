from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views import View
from ..models import App
import logging

logger = logging.getLogger(__name__)


@method_decorator(login_required(login_url="/login"), name="dispatch")
class Home(View):
    def get(self, request):
        apps = App.objects.all()
        web_apps = {}
        for app in apps:
            web_apps[app.name] = {
                "icon": "bi bi-chat-fill",
                "name": app.name,
                "description": app.description,
                "redirect_url": reverse(app.redirect_url),
            }
        # web_apps = {
        #     "talk_to_ai": {
        #         "icon": "bi bi-chat-fill",
        #         "name": "Talk to AI",
        #         "description": "Talk to AI is a web application that allows you to talk to an AI.",
        #         "redirect_url": reverse("public:talk-to-ai"),
        #     },
        # }

        logger.debug(f"web_apps {web_apps}")

        return render(request, "core/home.html", {"web_apps": web_apps})

    def post(self, request):
        pass
