import re
from typing import List
from django.utils.safestring import mark_safe
from .. import models


CODE_START_DELIM = '['
CODE_END_DELIM = ']'

# image pattern looks like '[image filenamewihtoutpath.ext]'
IMAGE_KEYWORD = 'image'
IMAGE_PATTERN = re.compile('(\\[{0} \\w+\\.\\w+\\])'.format(IMAGE_KEYWORD))

# caption pattern looks like '[caption "caption text here"]'
CAPTION_KEYWORD = 'caption'
CAPTION_PATTERN = re.compile('\\[{0} \".+\"\\]'.format(CAPTION_KEYWORD))

# sources look like '[source https://mysource.something]'
SOURCE_KEYWORD = 'source'
SOURCE_PATTERN = re.compile('(\\[{0} http.*?\\])'.format(SOURCE_KEYWORD))
SOURCE_LINK_MAX_CHARS = 30         # max length for links in sources

# links look like '[link "link text" https://nonsource.something]'
LINK_KEYWORD = 'link'
LINK_PATTERN = re.compile('(\\[{0} \".+\" http.*?\\])'.format(LINK_KEYWORD))


def handle_images(page_item: models.PageTopic):
    image_matches = IMAGE_PATTERN.findall(page_item.summary_text)

    # replace image patterns with image HTML
    for image_match in image_matches:
        image_file = image_match.split(' ')[1].replace(CODE_END_DELIM, '')
        image_html = '<div style="text-align:center"><img style="width: 60%" class="rounded" ' \
                     'src="static/corwin/images/{0}" class="img-fluid"></div>'.format(image_file)
        page_item.summary_text = page_item.summary_text.replace(image_match, image_html)


def handle_captions(page_item: models.PageTopic):
    caption_matches = CAPTION_PATTERN.findall(page_item.summary_text)

    # replace captions with caption text
    for caption_match in caption_matches:
        caption_text = caption_match.replace(CAPTION_KEYWORD, '')\
            .replace(CODE_START_DELIM, '')\
            .replace(CODE_END_DELIM,'')\
            .replace('"','')

        caption_html = '<div class="caption-text">{0}</div>'.format(caption_text)
        page_item.summary_text = page_item.summary_text.replace(caption_match, caption_html)


def build_source_list(page_items: List[models.PageTopic]):
    # keep track of sources referenced in the text
    source_dict = {}
    source_num = 0

    for item in page_items:
        source_matches = SOURCE_PATTERN.findall(item.summary_text)
        for source_match in source_matches:
            source_match_spl = source_match.replace(CODE_START_DELIM, '').replace(CODE_END_DELIM, '').split(' ')

            # if this matches our source pattern, add it to the source dict
            if len(source_match_spl) == 2 and source_match_spl[0] == SOURCE_KEYWORD:

                url = source_match_spl[1]
                if source_match not in source_dict:
                    source_num += 1
                    source_dict[source_match] = SourceHyperlink(source_num=source_num, url=url)

    for item in page_items:
        for source_key in source_dict:
            new_text = item.summary_text.replace(source_key, '<sup><a href="{0}" target="_blank">[{1}]</a></sup>'.format(
                source_dict[source_key].url, source_dict[source_key].source_num))
            item.summary_text = new_text

        # mark safe all html
        item.summary_text = mark_safe(item.summary_text)

    source_list = sorted([item for item in source_dict.values()], key=lambda x: x.source_num)

    return source_list


def handle_links(page_item: models.PageTopic):
    link_matches = LINK_PATTERN.findall(page_item.summary_text)

    # replace image patterns with image HTML
    for link_match in link_matches:
        text = link_match.split(' ')[1].replace(CODE_END_DELIM, '')
        url = link_match.split(' ')[2].replace(CODE_END_DELIM, '')
        url_html = '<a href="{0}" target="_blank">{1}</a>'.format(url, text)
        page_item.summary_text = page_item.summary_text.replace(link_match, url_html)


def create_page_contents(page_items: List[models.PageTopic]):
    """

    :param page_items:list of PageTopic items
    :return: Dict of parsed page topics and source dict
    """
    # TODO: look for a way to reduce number of loops through the page_items

    # iterate through the text for each text block
    for item in page_items:

        # handle images
        handle_images(item)

        # handle captions
        handle_captions(item)

    source_list = build_source_list(page_items)

    # mark safe all html
    for item in page_items:
        item.summary_text = mark_safe(item.summary_text)

    # context = PageContext(page_items, source_list)
    context = {'page_topics': page_items, 'source_list': source_list}
    return context


# class PageContext:
#     def __init__(self, page_items: List[models.PageTopic], source_list: List[object]):
#
#         self.page_items = page_items
#         self.source_list = source_list

class SourceHyperlink:
    max_display_chars = 30

    def __init__(self, source_num, url):

        self.source_num = source_num

        self.url = url

        self.display_text = url if len(url) < self.max_display_chars else "{0}...".format(url[:self.max_display_chars])

        self.hyperlink_tag = mark_safe('<a href="{0}" target="_blank">{1}</a>'.format(self.url, self.display_text))
