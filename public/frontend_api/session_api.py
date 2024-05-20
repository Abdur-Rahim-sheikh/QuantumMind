from django.views import View
from talk_to_ai.di.use_case import UseCase


class SessionAPI(View):
    def __init__(self):
        super().__init__()
        self.__use_case = UseCase()

    def get(self, request):
        pass

    def post(self, request):
        pass


# Path: public/frontend_api/emma_gpt_question_api.py
