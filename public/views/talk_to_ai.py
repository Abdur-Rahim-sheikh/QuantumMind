from django.shortcuts import render
from django.views import View

from public.utils import json_response
from services.di import UseCase
import json
import logging

logger = logging.getLogger(__name__)


class TalkToAI(View):
    def __init__(self):
        super().__init__()
        self.__use_case = UseCase()

    def get(self, request):
        return render(request, "talk_to_ai/home.html")

    def post(self, request):
        try:
            data = json.loads(request.body)
            query = data["query"]
            session_id = data["session_id"]

        except RuntimeError as e:
            return render(
                request, "talk_to_ai/home.html", {"error": f"Invalid message {e}"}
            )

        msg = self.__use_case.chat_generate_use_case(input_text=query)
        logger.debug(f"Generated response: {msg} for query: {query}")
        return json_response(
            message="successfully generated response",
            data={
                "response": msg,
            },
            status_code=200,
            success=True,
        )
