from django.shortcuts import render
from .models import PageHeadingTopic
from util.page_text_contents import create_page_text_contents


def index(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='home')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/index.html', context)