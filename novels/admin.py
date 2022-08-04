from django.contrib import admin
from .models import Novel

# Register your models here.
class NovelAdmin(admin.ModelAdmin):
    list_display = ('id','novel_title', 'novel_author', 'novel_status',
                    'novel_updated', 'novel_visible')
    list_editable = ('novel_visible',)
    list_display_links = ('novel_title', 'novel_author')

admin.site.register(Novel, NovelAdmin)