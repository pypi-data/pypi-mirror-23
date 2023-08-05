from verto.utils.HtmlParser import HtmlParser
from markdown.inlinepatterns import Pattern
from html import escape
import re


class RelativeLinkPattern(Pattern):
    '''Return a link element from the given match.

    Only matches:
        - Markdown links using []() syntax.
        - Links that don't start with:
            - http:
            - https:
            - ftp:
            - ftps:
            - mailto:
            - news:
    '''

    def __init__(self, ext, *args, **kwargs):
        '''
        Args:
            ext: An instance of the Markdown class.
        '''
        self.processor = 'relative-link'
        self.pattern = ext.processor_info[self.processor]['pattern']
        self.compiled_re = re.compile('^(.*?){}(.*)$'.format(self.pattern), re.DOTALL | re.UNICODE)
        self.template = ext.jinja_templates[self.processor]

    def handleMatch(self, match):
        ''' Inherited from Pattern. Accepts a match and returns an
        ElementTree element of a internal link.
        Args:
            match: The string of text where the match was found.
        Returns:
            An element tree node to be appended to the html tree.
        '''
        context = dict()
        context['link_path'] = escape(match.group('link_url'))
        context['text'] = match.group('link_text')

        html_string = self.template.render(context)
        parser = HtmlParser()
        parser.feed(html_string).close()
        return parser.get_root()
