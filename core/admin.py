from django.contrib import admin
from .models import Job, Application
from django.utils.html import format_html

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'salary', 'status', 'created_at']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job__title', 'name', 'email', 'applied_at', 'resume_link')
    list_filter = ('job', 'applied_at')
    search_fields = ('user__username', 'job__title')

    def resume_link(self, obj):
        if obj.resume:
            return format_html(f'<a href="{obj.resume.url}" target="_blank">Download</a>')
        return "-"
    resume_link.short_description = "Resume"