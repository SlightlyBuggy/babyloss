from django.contrib import admin
from .models import PageName, PageTopic, TopicType


class PageTopicAdmin(admin.ModelAdmin):

    list_display = ('page', 'topic_type', 'title_text', 'page_order')
    fieldsets = (
        (None, {
            'fields': ('page', 'page_order', 'topic_type', 'title_text', 'summary_text')
        }),
    )
    ordering = ['page_order']
    list_filter = ('page', 'topic_type')


class TopicTypeAdmin(admin.ModelAdmin):

    list_display = ['topic_type']


admin.site.register(PageTopic, PageTopicAdmin)
admin.site.register(PageName)
admin.site.register(TopicType, TopicTypeAdmin)
