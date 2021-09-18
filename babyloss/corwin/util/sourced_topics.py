import re
from django.utils.safestring import mark_safe

SOURCE_KEYWORD = 'source'
SOURCE_START_DELIM = '['
SOURCE_END_DELIM = ']'
OVERVIEW_NAME = 'overview'
BODY_NAME = 'body'


def sourcify(page_items):

    # keep track of sources referenced in the text
    source_pattern = re.compile('(\\[source http.*?\\])')
    source_dict = {}
    source_num = 0

    # iterate through the text for each text block
    for item in page_items:
        source_matches = source_pattern.findall(item.summary_text)

        for source_match in source_matches:
            source_match_spl = source_match.replace(SOURCE_START_DELIM, '').replace(SOURCE_END_DELIM,'').split(' ')

            # if this matches our source pattern, add it to the source dict
            if len(source_match_spl) == 2 and source_match_spl[0] == SOURCE_KEYWORD:

                url = source_match_spl[1]
                if source_match not in source_dict:
                    source_num += 1
                    source_dict[source_match] = {'url': url, 'source_num': source_num}

    # make another pass through the items and replace the source patterns with the HTMl we want
    for item in page_items:
        for source_key in source_dict:
            new_text = item.summary_text.replace(source_key, '<sup><a href="{0}" target="_blank">{1}</a></sup>'.format(
                source_dict[source_key]['url'], source_dict[source_key]['source_num']))
            item.summary_text = mark_safe(new_text)

    context = {'overview_items': [item for item in page_items if item.topic_type.topic_type == OVERVIEW_NAME],
               'body_items': [item for item in page_items if item.topic_type.topic_type == BODY_NAME],
               'sources': source_dict}
    return context
