from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


class AccountLogin(View):
    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        try:
            unique = request.POST.get("userNameOrEmail")
            password = request.POST.get("password")
        except RuntimeError as e:
            messages.warning(request, "Invalid login")
            return redirect("public:login")

        if "@" in unique:
            user = authenticate(request, email=unique, password=password)
        else:
            user = authenticate(request, username=unique, password=password)
        if user is not None:
            login(request, user)
            return redirect("public:home")
        else:
            messages.warning(request, "Invalid login")
            return redirect("public:login")
