from django.db import models


# name for each page
class PageName(models.Model):
    page_name = models.CharField(max_length=200)

    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name_plural = "Page Names"


# types of topics for each page
class TopicType(models.Model):
    topic_type = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_type

    class Meta:
        verbose_name_plural = "Topic Types"


# topics that can go on a page
class PageTopic(models.Model):
    page = models.ForeignKey(PageName, on_delete=models.DO_NOTHING)
    title_text = models.CharField(max_length=200)
    summary_text = models.TextField(max_length=200000)
    topic_type = models.ForeignKey(TopicType, on_delete=models.DO_NOTHING, default=1)
    page_order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Page Topics"






