from django.contrib import admin

from .models import User, Listing, Category, Bid, Comment, WatchList

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(WatchList)

# admin.site.register(Listing)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
