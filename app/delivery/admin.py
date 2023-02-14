from django.contrib import admin
from .models import Delivery, Package


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        "account",
        "order_number",
        "order_date",
        "created_at",
    )


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "delivery",
        "package_number",
        "tracking_number",
        "done",
        "created_at",
    )
