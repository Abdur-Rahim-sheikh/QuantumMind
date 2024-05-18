from django.contrib import admin

from public.models import Account, App

admin.site.site_header = "Quantum Mind"
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "password",
        "user_name",
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
