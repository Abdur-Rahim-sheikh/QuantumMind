from django.views import View
from django.shortcuts import render


class TalkToAI(View):
    def get(self, request):
        return render(request, "talk_to_ai/home.html")

    def post(self, request):
        pass
