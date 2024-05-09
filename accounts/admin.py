from django.contrib import admin

from accounts.models import Account

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
