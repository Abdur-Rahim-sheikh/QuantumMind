import json

from django.views import View

from ai_shortener.di.use_case import UseCase
from public.utils import json_response


class AIShortenerAPI(View):
    def __init__(self):
        super().__init__()
        self.__use_case = UseCase()

    def get(self, _):
        urls = self.__use_case.get_all_urls()
        return json_response(
            success=True,
            message="Successfully retrieved the response",
            data={"urls": urls},
        )

    def post(self, request):
        user_id = request.user.id
        data = json.loads(request.body)
        long_url = data.get("long_url")
        title = data.get("title", None)
        description = data.get("description", None)
        img = data.get("img", None)

        url = self.__use_case.shorten_url(
            long_url=long_url,
            title=title,
            description=description,
            img=img,
        )

        url.user_id = user_id
        url.save()

        return json_response(
            success=True,
            message="Successfully created the url",
            data={"url": url},
            status_code=201,
        )

    def delete(self, request):
        try:

            data = json.loads(request.body)
            url_id = data.get("url_id")
        except RuntimeError as e:
            return json_response(
                success=False, message="Invalid message", status_code=400
            )

        self.__use_case.delete_url(pid=url_id)
        return json_response(
            success=True, message="Successfully deleted the url", status_code=204
        )

    def put(self, request):
        try:
            data = json.loads(request.body)
            url_id = data.get("url_id")
            title = data.get("title", None)
            description = data.get("description", None)
            img = data.get("img", None)
        except RuntimeError as e:
            return json_response(
                success=False, message="Invalid message", status_code=400
            )

        self.__use_case.update_url(
            pid=url_id,
            title=title,
            description=description,
            img=img,
        )
        return json_response(
            success=True, message="Successfully updated the url", status_code=204
        )
