from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required(login_url="/login/"), name="dispatch")
class Home(View):
    def get(self, request):
        web_apps = {
            "talk_to_ai": {
                "name": "Talk to AI",
                "description": "Talk to AI is a web application that allows you to talk to an AI.",
                "redirect_url": "talk-to-ai",
            },
        }

        return render(request, "core/home.html", {"web_apps": web_apps})

    def post(self, request):
        pass
