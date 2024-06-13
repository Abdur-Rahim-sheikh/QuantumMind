from django.views import View
from django.shortcuts import render


class MyFriend(View):
    def get(self, request):
        return render(request, "my_friend/home.html")
