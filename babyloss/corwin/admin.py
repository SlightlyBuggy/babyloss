from django.contrib import admin
from .models import PageName, PageHeadingTopic, TopicType


class PageHeadingTopicAdmin(admin.ModelAdmin):

    list_display = ('title_text', 'page', 'topic_type')


class TopicTypeAdmin(admin.ModelAdmin):

    list_display = ['topic_type']


admin.site.register(PageHeadingTopic, PageHeadingTopicAdmin)
admin.site.register(PageName)
admin.site.register(TopicType, TopicTypeAdmin)
