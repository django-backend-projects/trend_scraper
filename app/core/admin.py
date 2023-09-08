from django.contrib import admin
from .models import (
    Account, ExcellAsanInfo, ExcellDeclInfo, FailedDeclar, Declaration,
    Interval,
)


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
admin.site.register(FailedDeclar)
admin.site.register(Declaration)

@admin.register(Interval)
class IntervalAdmin(admin.ModelAdmin):
    list_display = (
        "price",
        "start_interval",
        "end_interval",
        "is_active",
    )
    readonly_fields = ('created_at',)