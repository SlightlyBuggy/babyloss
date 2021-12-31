import re
from django.utils.safestring import mark_safe

SOURCE_KEYWORD = 'source'
CODE_START_DELIM = '['
CODE_END_DELIM = ']'
LINK_MAX_CHARS = 30
IMAGE_KEYWORD = 'image'
CAPTION_KEYWORD = 'caption'


def create_page_contents(page_items):

    # keep track of sources referenced in the text
    source_pattern = re.compile('(\\[source http.*?\\])')
    source_dict = {}
    source_num = 0

    # look for images in the text
    image_pattern = re.compile('(\\[image \\w+\\.\\w+\\])')

    # look for image captions in the text
    caption_pattern = re.compile('\\[caption \".+\"\\]')

    # iterate through the text for each text block
    for item in page_items:
        source_matches = source_pattern.findall(item.summary_text)
        image_matches = image_pattern.findall(item.summary_text)
        caption_matches = caption_pattern.findall(item.summary_text)

        # create dict of source patterns
        for source_match in source_matches:
            source_match_spl = source_match.replace(CODE_START_DELIM, '').replace(CODE_END_DELIM, '').split(' ')

            # if this matches our source pattern, add it to the source dict
            if len(source_match_spl) == 2 and source_match_spl[0] == SOURCE_KEYWORD:

                url = source_match_spl[1]
                if source_match not in source_dict:
                    source_num += 1
                    source_dict[source_match] = Hyperlink(source_num=source_num, url=url)

        # replace image patterns with image HTML
        for image_match in image_matches:
            image_file = image_match.split(' ')[1].replace(CODE_END_DELIM,'')
            image_html = '<img style="width: 100%" class="rounded" src="static/corwin/images/{0}" class="img-fluid">'.format(image_file)
            item.summary_text = mark_safe(item.summary_text.replace(image_match, image_html))

        # replace captions with caption text
        for caption_match in caption_matches:
            caption_text = caption_match.replace(CAPTION_KEYWORD, '').replace(CODE_START_DELIM, '').replace(CODE_END_DELIM, '').replace('"','')
            caption_html = '<div class="caption-text">{0}</div>'.format(caption_text)
            item.summary_text = mark_safe(item.summary_text.replace(caption_match, caption_html))

    # make another pass through the items and replace the source patterns with the HTMl we want
    for item in page_items:
        for source_key in source_dict:
            new_text = item.summary_text.replace(source_key, '<sup><a href="{0}" target="_blank">{1}</a></sup>'.format(
                source_dict[source_key].url, source_dict[source_key].source_num))
            item.summary_text = mark_safe(new_text)

        # mark safe all html
        item.summary_text = mark_safe(item.summary_text)

    source_list = sorted([item for item in source_dict.values()], key=lambda x: x.source_num)

    context = {'page_topics': page_items,
               'source_list': source_list}
    return context


class Hyperlink:
    max_display_chars = 30

    def __init__(self, source_num, url):

        self.source_num = source_num

        self.url = url

        self.display_text = url if len(url) < self.max_display_chars else "{0}...".format(url[:self.max_display_chars])

        self.hyperlink_tag = mark_safe('<a href="{0}" target="_blank">{1}</a>'.format(self.url, self.display_text))
