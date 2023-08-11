from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_at', 'modified_at', 'image_display']
    list_filter = ['auction', 'creation_date']

    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Вернуть возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )


admin.site.register(Advertisement, AdvertisementAdmin)

# Register your models here.
