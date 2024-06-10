from django.shortcuts import render
from django.views import View

from public.utils import json_response
from services.di import UseCase


class TalkToAI(View):
    def __init__(self):
        super().__init__()
        self.__use_case = UseCase()

    def get(self, request):
        return render(request, "talk_to_ai/home.html")

    def post(self, request):
        try:
            session_id = request.POST.get("session_id")
            query = request.POST.get("query")
        except RuntimeError as e:
            return render(
                request, "talk_to_ai/home.html", {"error": f"Invalid message {e}"}
            )

        msg = self.__use_case.chat_generate_use_case(input_text=query)
        return json_response(
            message="successfully generated response",
            data={
                "response": msg,
            },
            status_code=200,
            success=True,
        )
