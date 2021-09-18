from django.shortcuts import render
from .models import PageHeadingTopic
from util.sourced_topics import sourcify


def index(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='home')

    context = sourcify(page_items)

    return render(request, 'corwin/index.html', context)