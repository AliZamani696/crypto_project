from django.contrib import admin
from .models import WatchList


@admin.register(WatchList)
class admin(admin.ModelAdmin):
    list_display = ('user', 'crypto_symbol', 'target_price', 'created_at')
    search_fields = ('user__username', 'crypto_symbol')
    list_filter = ('created_at',)

