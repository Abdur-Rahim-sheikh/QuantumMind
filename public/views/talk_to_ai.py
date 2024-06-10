from django.views import View
from django.shortcuts import render
from services.di import UseCase
from public.utils import json_response


class TalkToAI(View):
    def __init__(self):
        super().__init__()
        self.__use_case = UseCase()

    def get(self, request):
        return render(request, "talk_to_ai/home.html")

    def post(self, request):
        try:
            message = request.POST.get("message")
        except RuntimeError as e:
            return render(request, "talk_to_ai/home.html", {"error": "Invalid message"})

        msg = self.__use_case.chat_generate_use_case(input_text=message)
        return json_response(
            message="success",
            data={
                "response": msg,
            },
            status_code=200,
        )
