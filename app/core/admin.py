from django.contrib import admin
from .models import Account, ExcellAsanInfo, ExcellDeclInfo


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "email",
        "password",
        "processed_at"
    )
    search_fields = ('client_id', 'email')
    list_filter = ('processed_at',)


admin.site.register(ExcellAsanInfo)
admin.site.register(ExcellDeclInfo)