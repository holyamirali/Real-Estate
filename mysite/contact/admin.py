from django.contrib import admin
from .models import Order

class ContactAdmin(admin.ModelAdmin):
    list_display    =   ("listing_name", "listing_id", "client_name")

admin.site.register(Order, ContactAdmin)