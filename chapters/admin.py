from django.contrib import admin
from .models import Chapter
from django_summernote.admin import SummernoteModelAdmin

class ChapterAdmin(SummernoteModelAdmin):
    list_display = ('id','chapter_number', 'chapter_novel',
                    'chapter_title', 'chapter_updated', 'chapter_visible')
    list_editable =  ('chapter_visible', 'chapter_updated')
    list_display_links = ('chapter_number', 'chapter_novel', 'chapter_title')


admin.site.register(Chapter, ChapterAdmin)

