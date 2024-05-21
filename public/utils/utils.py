from django.forms import Form, ModelForm
from django.http import JsonResponse


def json_response(
    success: bool,
    message: str,
    data: dict | list | None = None,
    errors: list[str] | None = None,
    status_code: int = 200,
) -> JsonResponse:
    return JsonResponse(
        data={
            "success": success,
            "message": message,
            "data": data,
            "errors": errors if errors else [],
        },
        status=status_code,
    )


def get_form_error(form: Form | ModelForm) -> list[str]:
    error_list = []
    for title, errors in form.errors.get_json_data().items():
        title = " ".join([word.title() for word in title.split("_")])
        for error in errors:
            error_list.append(f"{title}: {error.get('message')}")

    return error_list


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
