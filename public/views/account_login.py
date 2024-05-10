from django.views import View
from django.shortcuts import render


class AccountLogin(View):
    def get(self, request):
        return render(request, "accounts/login.html")
