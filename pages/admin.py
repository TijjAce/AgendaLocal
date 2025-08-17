
from django.utils.html import format_html
from django.contrib import admin
from .models import Page
from mptt.admin import MPTTModelAdmin

@admin.register(Page)
class PageAdmin(MPTTModelAdmin):
    list_display = ('title', 'slug', 'parent', 'published', 'created_at', 'view_link')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def view_link(self, obj):
        return format_html('<a href="{}" target="_blank">Voir</a>', obj.get_absolute_url())
    view_link.short_description = "Voir"



