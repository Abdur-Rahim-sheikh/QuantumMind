from django.shortcuts import render
from django.views import View

from public.utils import json_response
from services.di import ServiceUseCase
from talk_to_ai.di import UseCase
import json


class TalkToAI(View):
    def __init__(self):
        super().__init__()
        self.__service_use_case = ServiceUseCase()
        self.__use_case = UseCase()

    def get(self, request):
        return render(request, "talk_to_ai/home.html")

    def post(self, request):
        try:
            data = json.loads(request.body)
            user_id = request.user.id
            query = data["query"]
            session_id = data["session_id"]

        except RuntimeError as e:
            return render(
                request, "talk_to_ai/home.html", {"error": f"Invalid message {e}"}
            )
        session = self.__use_case.get_session(user_id=user_id, session_id=session_id)
        msg = self.__service_use_case.chat_generate_use_case(input_text=query)
        session.conversations += [query, msg]
        self.__use_case.update_session(session)

        return json_response(
            message="successfully generated response",
            data={
                "response": msg,
            },
            status_code=200,
            success=True,
        )
