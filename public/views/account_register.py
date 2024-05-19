import logging

from django.contrib import messages
from ..forms import AccountCreationForm
from django.shortcuts import render, redirect
from django.views import View

logger = logging.getLogger(__name__)


class AccountRegister(View):
    def get(self, request):
        return render(request, "accounts/register.html")

    def post(self, request):
        form = AccountCreationForm(
            {
                "username": request.POST.get("userName"),
                "password1": request.POST.get("password"),
                "password2": request.POST.get("confirmPassword"),
                "email": request.POST.get("email"),
                "first_name": request.POST.get("firstName"),
                "last_name": request.POST.get("lastName"),
            }
        )
        if form.is_valid():
            form.save()
        else:
            for field in form:
                for error in field.errors:
                    logger.error(f"Signup Error: {field.name=}\n{error=}")
            messages.warning(request, "Could not create account")
            return redirect("public:signup")
        return redirect("public:login")
