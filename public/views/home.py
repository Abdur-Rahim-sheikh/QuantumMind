from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class Home(View):
    @login_required(login_url="/login/")
    def get(self, request):
        return render(request, "core/home.html")
