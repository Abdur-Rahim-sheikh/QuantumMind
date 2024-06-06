from django.views import View

from public.utils import json_response
from talk_to_ai.di.use_case import UseCase


class SessionsAPI(View):
    def __init__(self):
        super().__init__()
        self.__use_case = UseCase()

    def get(self, request):
        user_id = request.user.id
        # check if the user_id exists in the database in future!
        sessions = self.__use_case.get_all_sessions(user_id=user_id)
        return json_response(
            success=True,
            message="Successfully retrieved the response",
            data={"sessions": sessions},
        )

    def post(self, request):
        user_id = request.user.id
        data = request.data
        session_name = data.get("session_name")
        self.__use_case.create_session(user_id=user_id, session_name=session_name)
        return json_response(
            success=True,
            message="Successfully created the session",
        )


# Path: public/frontend_api/emma_gpt_question_api.py
