from django.contrib import admin
from .models import GuestMessage

@admin.register(GuestMessage)
class GuestMessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'written_at')