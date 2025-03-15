from typing import Any
from django.contrib import admin,messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from posApp.models import Category, Creditor, Debtors, Products, Sales, inventory, salesItems,Stock

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
admin.site.register(inventory)
admin.site.register(Debtors)
admin.site.register(Creditor)
# admin.site.register(Employees)
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    # list_display = ('stock_code','description','quantity_available','recorded_value')
    search_fields = ('stock_code','description')

    def get_queryset(self, request):
        query_set = super().get_queryset(request)
        low_stock_item = [Stock for Stock in query_set if Stock.is_below_reorder_level()]
        if low_stock_item:
            messages.warning(request,"some stock levels are low!")
        return query_set