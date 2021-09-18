from django.shortcuts import render
from .models import PageHeadingTopic
from util.db_to_html_with_sources import overview_body_and_sources


def index(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='home')

    context = overview_body_and_sources(page_items)

    return render(request, 'corwin/index.html', context)