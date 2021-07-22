from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display        = ("name" , "phone" , "email")
    list_display_links  = ("name",)
    list_editable       = ("phone" , "email")

admin.site.register(Realtor, RealtorAdmin)