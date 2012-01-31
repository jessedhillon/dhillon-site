from pyramid.url import route_url, static_url
from pyramid.threadlocal import get_current_request, get_current_registry

from markdown import Markdown
from BeautifulSoup import BeautifulSoup, NavigableString

from dhillon_site.lib.util import slug

def static_url_filter(path, *elements, **kw):
    request = get_current_request()
    return static_url(path, request, *elements, **kw)

def markdown_filter(s):
    return Markdown().convert(s)

def flatten_html_filter(html):
    if isinstance(html, basestring):
        soup = BeautifulSoup(html)
    else:
        soup = html

    for tag in soup.findAll(True):
        s = ""
        for c in tag.contents:
            if not isinstance(c, NavigableString):
                c = flatten_html_filter(c)
            s += unicode(c)
        tag.replaceWith(s)
    return soup.renderContents()

def excerpt_filter(s, chars=140, trailer='&hellip;'):
    n = 0
    excerpt = []
    for w in s.split(' '):
        if n > chars:
            break

        excerpt.append(w)
        n += len(w)

    return ' '.join(excerpt) + (trailer if n > chars else '')

def slug_filter(s):
    return slug(s)
