from django.contrib import admin
from .models import Listings

class ListingsAdmin(admin.ModelAdmin):
    list_display        = ("title" , "realtor" , "price" , "photo_main")
    list_display_links  = ("title" , "realtor" , "photo_main")
    list_editable       = ("price",)
    
admin.site.register(Listings, ListingsAdmin)
