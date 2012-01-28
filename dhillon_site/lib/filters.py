from pyramid.url import route_url, static_url
from pyramid.threadlocal import get_current_request, get_current_registry

def static_url_filter(path, *elements, **kw):
    request = get_current_request()
    return static_url(path, request, *elements, **kw)

