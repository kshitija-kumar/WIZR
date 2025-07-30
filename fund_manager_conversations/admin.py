from django.contrib import admin
from .models import Meeting

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'meeting_type', 'meeting_date')
    search_fields = ('title', 'content')
    fields = ('title', 'meeting_type', 'pdf_file', 'audio_file', 'content', 'meeting_date')
