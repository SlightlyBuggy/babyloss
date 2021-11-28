from django.shortcuts import render
from .models import PageHeadingTopic
from corwin.util.page_text_contents import create_page_text_contents


def index(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='home')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/index.html', context)


def babyloss(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='babyloss')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/babyloss.html', context)


def resources_expecting(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='resources_expecting')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/resources_expecting.html', context)


def resources_loss(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='resources_loss')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/resources_loss.html', context)


def resources_doulas(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='resources_doulas')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/resources_doulas.html', context)


def resources_providers(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='resources_providers')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/resources_providers.html', context)


def resources_loved(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='resources_loved')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/resources_loved.html', context)


def resources_employers(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='resources_employers')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/resources_employers.html', context)


def corwin_story(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='corwin_story')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/corwin_story.html', context)


def about(request):

    page_items = PageHeadingTopic.objects.filter(page__page_name='about')

    context = create_page_text_contents(page_items)

    return render(request, 'corwin/about.html', context)