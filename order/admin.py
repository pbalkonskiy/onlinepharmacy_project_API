from django.contrib import admin

from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "key",
        "customer_id",
        "numb_of_positions",
        "total_price",
        "date",
        "delivery_method",
        "payment_method",
        "payment_status",
        "is_paid",
        "in_progress",
    )
    list_filter = (
        "is_paid",
        "customer_id",
        "date",
        "payment_status",
        "delivery_method",
    )
    empty_value_display = "undefined"
