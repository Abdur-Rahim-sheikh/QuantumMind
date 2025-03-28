from django.contrib import admin

from public.models import Account, App, ChatSession, CustomModel, BotFriend, Url

admin.site.site_header = "Quantum Mind"
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "password",
        "username",
        "is_superuser",
    )


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "version",
        "redirect_url",
        "img_base64",
    )


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "chat_name",
        "conversations",
    )


@admin.register(CustomModel)
class CustomModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "gender",
        "age",
        "profession",
        "model_from",
        "more_info",
        "parameters",
    )


@admin.register(BotFriend)
class BotFriendAdmin(admin.ModelAdmin):
    list_display = ("user", "custom_model", "conversations")

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "description",
        "long_url",
        "short_url",
        "ai_url",
    )