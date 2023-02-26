from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "email",
        "password",
        "processed_at"
    )
