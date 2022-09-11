# access to Shoes in admin site
from django.contrib import admin
from .models import ShoePair, Category


@admin.register(ShoePair)
class ShoeAdmin(admin.ModelAdmin):
    # Display info in admin site
    list_display = ('shoe_name', 'trader', 'status', 'created_on')
    search_fields = ['shoe_name', 'trader']
    prepopulated_fields = {'slug': ('trader_name',)}
    list_filter = ('trader', 'created_on')
    actions = ['publish_trade']

    def publish_trade(self, request, queryset):
        # function to approve pending trade post
        queryset.update(status=1)

admin.site.register(Category)
